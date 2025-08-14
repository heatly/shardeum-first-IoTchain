import os
from web3 import Web3
from solcx import compile_source, install_solc

# Install specific solc version
install_solc('0.8.0')

# Environment variables
RPC = "https://api-unstable.shardeum.org"
CHAIN_ID = 8080
PRIVATE_KEY = "0xc25756fa8ff8a7a82a3c539748632080c00e417d45fcee0058149ead4dde9f7d"
ACCOUNT_ADDRESS = Web3().eth.account.from_key(PRIVATE_KEY).address

# Connect to Shardeum
web3 = Web3(Web3.HTTPProvider(RPC))
if not web3.is_connected():
    raise Exception("❌ Failed to connect to Shardeum RPC")

print(f"Connected to Shardeum. Account: {ACCOUNT_ADDRESS}")

# Solidity smart contract
contract_source = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IoTRelay {
    bool public relayState;

    event RelayToggled(bool state);

    function toggleRelay(bool _state) public {
        relayState = _state;
        emit RelayToggled(_state);
    }
}
'''

# Compile contract
compiled_sol = compile_source(contract_source, output_values=['abi', 'bin'])
contract_id, contract_interface = compiled_sol.popitem()
abi = contract_interface['abi']
bytecode = contract_interface['bin']

# Deploy
IoTRelay = web3.eth.contract(abi=abi, bytecode=bytecode)
nonce = web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
transaction = IoTRelay.constructor().build_transaction({
    'chainId': CHAIN_ID,
    'gas': 2000000,
    'gasPrice': web3.to_wei('2', 'gwei'),
    'nonce': nonce
})
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
print(f"Deploying... TX hash: {tx_hash.hex()}")

tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"✅ Contract deployed at: {tx_receipt.contractAddress}")
