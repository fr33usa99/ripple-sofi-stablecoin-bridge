# Ripple–SoFi Stablecoin Bridge CLI Demo

Author: Adam Sanchez  
Date: June 2025  
Proof-of-concept for routing USDC → XRP → EURC under GENIUS Act compliance.

## Modules
- `usdc_mock.py`: Mocks a SoFi wallet holding USDC
- `xrp_bridge.py`: Sends XRP cross-border
- `dex_swap_mock.py`: Mocks DEX swap of XRP to EURC
- `compliance_logger.py`: Logs tx info to `compliance_log.json`
- `run_demo.py`: Full transaction runner
