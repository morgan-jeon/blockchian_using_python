from datetime import datetime 
from crypto import crypto

class Block:
    def __init__(self, transactions, prev_hash, nonce = 0):
        self.timestamp = datetime.now()
        self.transaction = transactions
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def update_hash(self):
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_content = str(self.timestamp) + str(self.transaction) + str(self.prev_hash) + str(self.nonce)
        block_hash = crypto.hexhash(block_content)
        return block_hash

    def __repr__(self):
        return f'{self.timestamp}: {self.hash} {self.transaction}'