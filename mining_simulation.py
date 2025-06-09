import hashlib
import time

class Block:
    def __init__(self, data):
        self.data = data
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.timestamp) + self.data + str(self.nonce)).encode()).hexdigest()

    def mine_block(self, difficulty):
        print("Mining block...")
        start_time = time.time()
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        end_time = time.time()
        print(f"Block mined! Nonce: {self.nonce}, Hash: {self.hash}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")

block = Block("Important Data")
block.mine_block(4)