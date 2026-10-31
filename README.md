# Functional Python Blockchain & Cryptocurrency Simulation

A lightweight, educational cryptocurrency ledger built from scratch in **pure Python** using a **functional (procedural) approach**—completely avoiding classes and object-oriented programming (For now, I will Implement it later). Blocks are represented as dictionaries and the ledger is a simple Python list.

---

##  Architecture & Core Components

The system relies on four primary functions and a command-line interface (CLI) workflow:

1. **`calculate_hash(block)`**
   * Takes a block dictionary, temporarily removes its `'hash'` key to prevent recursive hashing, serializes it into a sorted JSON string, and returns its SHA-256 cryptographic signature.
2. **`mine_block(block, difficulty)`**
   * Implements **Proof-of-Work**. It runs a `while` loop that increments a `nonce` until the block's hash starts with the required number of leading zeros (determined by the difficulty).
3. **`create_block(data, prev_hash, index)`**
   * Assembles the block skeleton (index, timestamp, data, previous hash, initial nonce) and immediately hands it over to the miner to find a valid hash.
4. **`is_chain_valid(blockchain)`**
   * Iterates through the chain to guarantee immutability by verifying that every block's hash is authentic and its `prev_hash` correctly points to the preceding block.

---

##  Build Flow & Interactive Workflow

* **Startup & Genesis Block:** The script initializes an empty `blockchain` list and automatically creates and mines a hardcoded **Genesis Block** (`prev_hash = "0"`). This ensures a valid starting point exists before any user interactions.
* **The Mempool (`pending_transactions`):** Users can add transactions (sender, recipient, amount) via the CLI menu. These sit in a temporary queue rather than being mined instantly.
* **Batch Mining:** When the user triggers the mining option, all collected pending transactions are bundled together into a **single new block**, mined via Proof-of-Work, and securely appended to the ledger.
* **Validation & Tampering Detection:** Users can verify the integrity of the chain at any time to ensure no data has been modified.

---

##  Challenges Faced & How They Were Solved

### 1. The Empty Chain IndexError (`blockchain[-1]`)
* **The Problem:** When trying to grab `last_hash = blockchain[-1]["hash"]` for the first user transaction, Python threw an `IndexError` because the list was completely empty.
* **The Solution:** Realized that a blockchain *must* have a pre-existing root. Implemented the hardcoded **Genesis Block** creation step at the very beginning of execution so a valid last block always exists.

### 2. The Hash Chicken-and-Egg Problem
* **The Problem:** A block dictionary needs to contain its own `hash` key, but hashing a dictionary that already contains that hash creates a circular dependency.
* **The Solution:** Used `.copy()` and `.pop('hash', None)` inside `calculate_hash()` so the script temporarily strips the hash container away while generating the cryptographic signature.

### 3. Transitioning from Single to Batched Transactions
* **The Problem:** Initially, looping through pending transactions created a separate, individual block for every single transaction, which differs from how real cryptocurrencies batch data.
* **The Solution:** Refactored the mining workflow to pass the *entire* list of pending transactions into a single `create_block()` call, properly simulating a real mempool block consolidation.

---

## 💻 How to Run

1. Make sure you have Python installed.
2. Run the script:
   ```bash
   python blockchain.py
