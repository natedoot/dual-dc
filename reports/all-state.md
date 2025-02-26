# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed | Total Tests Skipped |
| ----------- | ------------------ | ------------------ | ------------------- |
| 712 | 704 | 8 | 0 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| dc1-leaf1a | 71 | 70 | 1 | 0 | Interfaces | - |
| dc1-leaf1b | 71 | 70 | 1 | 0 | Interfaces | - |
| dc1-leaf1c | 6 | 6 | 0 | 0 | - | - |
| dc1-leaf2a | 78 | 77 | 1 | 0 | Interfaces | - |
| dc1-leaf2b | 78 | 77 | 1 | 0 | Interfaces | - |
| dc1-leaf2c | 6 | 6 | 0 | 0 | - | - |
| dc1-spine1 | 23 | 23 | 0 | 0 | - | - |
| dc1-spine2 | 23 | 23 | 0 | 0 | - | - |
| dc2-leaf1a | 71 | 70 | 1 | 0 | Interfaces | - |
| dc2-leaf1b | 71 | 70 | 1 | 0 | Interfaces | - |
| dc2-leaf1c | 6 | 6 | 0 | 0 | - | - |
| dc2-leaf2a | 78 | 77 | 1 | 0 | Interfaces | - |
| dc2-leaf2b | 78 | 77 | 1 | 0 | Interfaces | - |
| dc2-leaf2c | 6 | 6 | 0 | 0 | - | - |
| dc2-spine1 | 23 | 23 | 0 | 0 | - | - |
| dc2-spine2 | 23 | 23 | 0 | 0 | - | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 80 | 80 | 0 | 0 |
| Connectivity | 212 | 212 | 0 | 0 |
| Interfaces | 256 | 248 | 8 | 0 |
| MLAG | 8 | 8 | 0 | 0 |
| Routing | 140 | 140 | 0 | 0 |
| System | 16 | 16 | 0 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 37 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel5 - PortChannel dc1-leaf1-server1 = 'up' | FAIL | Port-Channel5 - Expected: up/up, Actual: down/lowerLayerDown |
| 108 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel5 - PortChannel dc1-leaf1-server1 = 'up' | FAIL | Port-Channel5 - Expected: up/up, Actual: down/lowerLayerDown |
| 192 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel5 - SERVER_dc1-leaf2-server1 = 'up' | FAIL | Port-Channel5 - Expected: up/up, Actual: down/lowerLayerDown |
| 270 | dc1-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel5 - SERVER_dc1-leaf2-server1 = 'up' | FAIL | Port-Channel5 - Expected: up/up, Actual: down/lowerLayerDown |
| 393 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel5 - SERVER_dc2-leaf1-server1_Bond1 = 'up' | FAIL | Port-Channel5 - Expected: up/up, Actual: down/lowerLayerDown |
| 464 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel5 - SERVER_dc2-leaf1-server1_Bond1 = 'up' | FAIL | Port-Channel5 - Expected: up/up, Actual: down/lowerLayerDown |
| 548 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel5 - SERVER_dc2-leaf2-server1 = 'up' | FAIL | Port-Channel5 - Expected: up/up, Actual: down/lowerLayerDown |
| 626 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel5 - SERVER_dc2-leaf2-server1 = 'up' | FAIL | Port-Channel5 - Expected: up/up, Actual: down/lowerLayerDown |

