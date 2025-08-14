# Shardeum IoT Relay Control

## Files
- `deploy_contract.py`: Deploys the IoT relay smart contract to Shardeum.
- `interact_contract.py`: Interact with the deployed contract (toggle relay, read state).
- `index.html`: Simple web UI to toggle relay via MetaMask.
- `esp32_relay.ino`: ESP32 code to poll the blockchain for relay state.
- `.env`: Stores RPC URL, Chain ID, and Private Key.

## Usage
```bash
pip install web3 py-solc-x
python deploy_contract.py
python interact_contract.py
```
