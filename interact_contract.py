from web3 import Web3

RPC = "https://api-unstable.shardeum.org"
CHAIN_ID = 8080
PRIVATE_KEY = "0xc25756fa8ff8a7a82a3c539748632080c00e417d45fcee0058149ead4dde9f7d"
ACCOUNT_ADDRESS = Web3().eth.account.from_key(PRIVATE_KEY).address
CONTRACT_ADDRESS = "0xe8C3DF29503a5c87b2dd06cd7Ab512d74761C363"

# IoT Relay ABI
abi = [
    {
        "inputs":[{"internalType":"bool","name":"_state","type":"bool"}],
        "name":"toggleRelay",
        "outputs":[],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[],
        "name":"relayState",
        "outputs":[{"internalType":"bool","name":"","type":"bool"}],
        "stateMutability":"view",
        "type":"function"
    }
]

web3 = Web3(Web3.HTTPProvider(RPC))

def toggle_relay(state: bool):
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)
    nonce = web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    tx = contract.functions.toggleRelay(state).build_transaction({
        'chainId': CHAIN_ID,
        'gas': 200000,
        'gasPrice': web3.to_wei('2', 'gwei'),
        'nonce': nonce
    })
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"Relay toggle TX: {tx_hash.hex()}")
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("✅ Relay state updated")

def get_relay_state():
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)
    state = contract.functions.relayState().call()
    print(f"Relay is {'ON' if state else 'OFF'}")
    return state

if __name__ == "__main__":
    get_relay_state()
    toggle_relay(True)
    get_relay_state()
