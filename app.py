from flask import Flask, render_template, request, redirect, url_for, flash
import yaml
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

MASTER_YAML_FILE = "group_vars/NETWORK_SERVICES.yml"  # Define the master YAML file

def load_yaml(file_path):
    """Loads YAML data from a file."""
    if not os.path.exists(file_path):
        return {}  # Return empty dict if file doesn't exist
    with open(file_path, "r") as f:
        return yaml.safe_load(f) or {}

def save_yaml(file_path, data):
    """Saves YAML data to a file."""
    with open(file_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

def append_to_yaml(master_file, network_services_key, vrf_name, new_svi):
    """Appends SVI data to the specified tenant and VRF in the master YAML file,
    ensuring VRF VNI consistency across all tenants, and creating a new tenant if needed."""

    master_yaml = load_yaml(master_file)

    # Step 1: If tenant does not exist, create it
    if network_services_key not in master_yaml:
        master_yaml[network_services_key] = [
            {
                "name": network_services_key,
                "mac_vrf_vni_base": 10000,  # Default base value for new tenants
                "vrfs": []
            }
        ]
        flash(f"New tenant {network_services_key} created.", "info")

    # Step 2: Find if the VRF already exists in ANY tenant and reuse its vrf_vni
    existing_vrf_vni = None
    last_used_vrf_vni = 0  # Track highest VNI used

    for tenant_name, tenant_list in master_yaml.items():
        if isinstance(tenant_list, list) and len(tenant_list) > 0:
            tenant = tenant_list[0]  # Get the first tenant entry

            if "vrfs" in tenant and isinstance(tenant["vrfs"], list):
                for vrf in tenant["vrfs"]:
                    if isinstance(vrf, dict):
                        last_used_vrf_vni = max(last_used_vrf_vni, vrf.get("vrf_vni", 0))
                        if vrf.get("name") == vrf_name:
                            existing_vrf_vni = vrf["vrf_vni"]

    # If VRF does not exist anywhere, assign a new vrf_vni
    if existing_vrf_vni is None:
        existing_vrf_vni = last_used_vrf_vni + 1

    # Step 3: Ensure the current tenant exists (this should always be true now)
    tenant_list = master_yaml[network_services_key]
    if not isinstance(tenant_list, list) or len(tenant_list) == 0:
        flash(f"Invalid structure for {network_services_key} in NETWORK_SERVICES.yml.", "danger")
        return

    tenant = tenant_list[0]

    # Ensure VRFs exist in this tenant
    if "vrfs" not in tenant or not isinstance(tenant["vrfs"], list):
        tenant["vrfs"] = []

    vrf_list = tenant["vrfs"]

    # Step 4: Find or create the VRF within this tenant
    vrf = next((v for v in vrf_list if isinstance(v, dict) and v.get("name") == vrf_name), None)

    if not vrf:
        vrf = {"name": vrf_name, "vrf_vni": existing_vrf_vni, "svis": []}
        vrf_list.append(vrf)
        flash(f"New VRF {vrf_name} created in {network_services_key} with vrf_vni {existing_vrf_vni}.", "info")

    # Ensure "svis" exists in the VRF and is a list
    if "svis" not in vrf or not isinstance(vrf["svis"], list):
        vrf["svis"] = []

    # Step 5: Check if VLAN ID already exists
    if any(svi["id"] == new_svi["id"] for svi in vrf["svis"] if isinstance(svi, dict)):
        flash(f"SVI with VLAN ID {new_svi['id']} already exists in VRF {vrf_name}.", "danger")
        return

    # Step 6: Append the new SVI
    vrf["svis"].append(new_svi)
    save_yaml(master_file, master_yaml)
    flash("SVI successfully added!", "success")


@app.route("/", methods=["GET", "POST"])
def index():
    master_yaml = load_yaml(MASTER_YAML_FILE)
    tenants = sorted(master_yaml.keys())  # Get list of existing tenants

    # Get a list of ALL VRFs across ALL tenants
    all_vrfs = set()
    for tenant_list in master_yaml.values():
        if isinstance(tenant_list, list):
            for tenant in tenant_list:
                if "vrfs" in tenant and isinstance(tenant["vrfs"], list):
                    all_vrfs.update(vrf["name"] for vrf in tenant["vrfs"])

    if request.method == "POST":
        network_services_key = request.form.get("business_unit")  # Tenant Key
        custom_tenant = request.form.get("custom_tenant")  # If new tenant is provided
        vrf_name = request.form.get("vrf_name")
        custom_vrf = request.form.get("custom_vrf")  # If new VRF is provided
        vlan_id = request.form.get("vlan_id")
        svi_name = request.form.get("svi_name")
        ip_address = request.form.get("ip_address")
        enabled = request.form.get("enabled")

        # Use custom tenant if provided
        if network_services_key == "custom" and custom_tenant:
            network_services_key = custom_tenant

        # Use custom VRF if provided
        if vrf_name == "custom" and custom_vrf:
            vrf_name = custom_vrf

        if not (network_services_key and vrf_name and vlan_id and svi_name and ip_address and enabled):
            flash("All fields are required!", "danger")
            return redirect(url_for("index"))

        try:
            vlan_id = int(vlan_id)
        except ValueError:
            flash("VLAN ID must be an integer.", "danger")
            return redirect(url_for("index"))

        # Convert enabled from string to boolean
        enabled = True if enabled.lower() == "true" else False

        new_svi = {
            "id": vlan_id,
            "name": svi_name,
            "ip_address": ip_address,
            "enabled": enabled
        }

        append_to_yaml(MASTER_YAML_FILE, network_services_key, vrf_name, new_svi)
        return redirect(url_for("index"))

    return render_template("form.html", tenants=tenants, all_vrfs=sorted(all_vrfs))

if __name__ == "__main__":
    app.run(debug=True)
