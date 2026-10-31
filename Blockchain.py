import hashlib
import time
import json

def calculate_hash(block):
    block_copy = block.copy()
    block_copy.pop('hash',None)
    block_string = json.dumps(block_copy, sort_keys=True).encode()

    return hashlib.sha256(block_string).hexdigest()

def create_block(data, prev_hash, index):
    timestamp = time.time()
    block = {
        'index':index,
        'timestamp':timestamp,
        'data':data,
        'prev_hash':prev_hash,
        'nonce':0,
        'hash':''
    }
    block['hash'] = calculate_hash(block)
    return block

def mine_block(block, difficulty):
    target = "0" * difficulty

    while not block['hash'].startswith(target):
        block['nonce'] += 1
        #print(calculate_hash(block))
        block['hash'] = calculate_hash(block)

    print(calculate_hash(block), "MINED")
    print("Block" ,block['index'] ,"mined! Nonce:", block['nonce'])
    return block

def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i-1]

        if current_block['hash'] != calculate_hash(current_block):
            print(f"Tampering detected! Hash mismatch at Block #{current_block['index']}")
            return False

        if i > 0 and current_block['prev_hash'] != previous_block['hash']:
            print(f"Broken chain! Invalid previous hash at Block #{current_block['index']}")
            return False
    return True


if __name__ == "__main__":

    blockchain = []
    difficulty = 2
    pending_transactions = []

    print("=" * 50)
    print("WELCOME TO MY CRYPTOCURRENCY!")
    print("=" * 50)

    print("Creating Genesis Block...")
    genesis_block = create_block("Genesis Bock Data", "0", 0)
    blockchain.append(genesis_block)

    while True:
        print()
        print("1. Add a transaction / Mine a new block")
        print("2. View the blockchain")
        print("3. Verify chain validity")
        print("4. Mine Blocks")
        print()
        try:
            ch = int(input("Enter Your Choice:"))
            if ch == 1:

                sender = input("Enter sender name: ")
                recipient = input("Enter recipient name: ")
                amount = float(input("Enter amount to transfer: "))

                pending_transactions.append({"sender": sender, "recipient": recipient, "amount": amount})


            elif ch == 2:
                for i in range(len(blockchain)):
                    print()
                    print("Block-",i+1)
                    print("Index -", blockchain[i].get("index"))
                    print("Timestamp -", blockchain[i].get("timestamp"))
                    print("Data -", blockchain[i].get("data"))
                    print("Previous Hash -", blockchain[i].get("prev_hash"))
                    print("Nonce -", blockchain[i].get("nonce"))
                    print("Hash -", blockchain[i].get("hash"))
                    print("-"*50)

            elif ch == 3:
                if is_chain_valid(blockchain):
                    print("The Chain is Vaild")

            elif ch == 4:
                if len(pending_transactions) > 0:
                    last_hash = blockchain[-1]["hash"]
                    new_block = create_block(pending_transactions, last_hash, len(blockchain))
                    mined_block = mine_block(new_block, difficulty)
                    blockchain.append(mined_block)
                    pending_transactions = []
                else:
                    print("No pending transaction to mine!")

        except ValueError:
            print("Please Enter A Integer Value:")
