from block import Block

class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.all_transaction = []
        self.genesis_block = Block({}, 0)
        self.chain.append(self.genesis_block)

    def proof_of_work(self, block, difficulty = 2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        return proof

    def add_block(self, transactions):
        prev_block_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, prev_block_hash)
        proof = self.proof_of_work(new_block)
        new_block.update_hash()
        self.chain.append(new_block)
        return proof, new_block

    def validate_chain(self):
        for i in range(1,len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.generate_hash():
                print('Current Block Not Valid')
                return False
            if previous.hash != previous.generate_hash():
                print('Prev Block not Valid')
                return False
            if current.prev_hash != previous.hash:
                return False
        return True