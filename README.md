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
🚀 Shardeum IoT Relay Control
World’s First IoT Control Project on the Shardeum Blockchain

This project integrates IoT relay hardware (ESP32) with Shardeum blockchain smart contracts, enabling secure, transparent, and decentralized device control over the internet.

🌟 Key Features
🥇 First of Its Kind
First IoT relay control project deployed on the Shardeum Chain — pioneering blockchain-powered IoT automation.

🔗 Blockchain Integration
Smart contract deployed on Shardeum EVM-compatible network for controlling relay states.

Immutable transaction logs for full transparency.

Only authorized wallet addresses can trigger device state changes.

⚡ Real-Time IoT Control
ESP32 microcontroller connected to relays receives state updates instantly from blockchain.

Supports ON/OFF commands for home automation, industrial processes, or smart farms.

🛡 Security First
Transactions signed using private keys (no central server storing sensitive credentials).

Immutable ledger ensures device control history is tamper-proof.

🌐 Cross-Platform
Works with Python scripts, ESP32 firmware, and web interfaces.

Compatible with any EVM-compatible blockchain (can be ported from Shardeum to Ethereum, Polygon, etc.).

🛠 Tech Stack
Smart Contract: Solidity

Blockchain: Shardeum Betanet/Sphinx Testnet

IoT Device: ESP32 with Relay Module

Backend: Python (Web3.py) for contract interaction

Firmware: Arduino C++ for ESP32 blockchain polling

📜 How It Works
Deploy the smart contract on Shardeum.

Call the contract functions via Python to set relay states.

ESP32 continuously checks the blockchain for state changes.

Relay switches ON/OFF based on blockchain command.
