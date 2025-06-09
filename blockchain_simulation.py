import hashlib
import time
from dataclasses import dataclass
from typing import Any, List

@dataclass
class Block:
    """A block in the blockchain containing data and cryptographic links."""
    index: int
    timestamp: float
    data: Any
    previous_hash: str
    nonce: int = 0
    
    def __post_init__(self):
        """Calculate the block's hash after initialization."""
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Generate a SHA-256 hash of the block's contents.
        
        Returns:
            str: Hexadecimal string representation of the hash
        """
        block_contents = (
            str(self.index) + 
            str(self.timestamp) + 
            str(self.data) + 
            str(self.previous_hash) + 
            str(self.nonce)
        )
        return hashlib.sha256(block_contents.encode()).hexdigest()

class Blockchain:
    """A simple blockchain implementation."""
    
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain: List[Block] = [self.create_genesis_block()]
    
    @staticmethod
    def create_genesis_block() -> Block:
        """Create the first block in the blockchain (genesis block)."""
        return Block(0, time.time(), "Genesis Block", "0")
    
    def add_block(self, data: Any) -> Block:
        """Add a new block to the blockchain.
        
        Args:
            data: The data to be stored in the new block
            
        Returns:
            Block: The newly created block
        """
        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self) -> bool:
        """Verify the integrity of the blockchain.
        
        Returns:
            bool: True if the blockchain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            
            if current_block.hash != current_block.calculate_hash():
                return False
                
            
            if current_block.previous_hash != previous_block.hash:
                return False
                
        return True
    
    def display_chain(self):
        """Print all blocks in the blockchain."""
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Data: {block.data}")
            print(f"  Hash: {block.hash}")
            print(f"  Prev Hash: {block.previous_hash}\n")


if __name__ == "__main__":

    blockchain = Blockchain()
    
    
    blockchain.add_block("Second Block")
    blockchain.add_block("Third Block")
    
    
    print("Initial Blockchain:")
    blockchain.display_chain()
    
    
    print(f"Blockchain valid: {blockchain.is_chain_valid()}")
    
    
    print("\nTampering with Block 1...")
    blockchain.chain[1].data = "Tampered Data"
    blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()
    
    
    print("\nAfter Tampering:")
    blockchain.display_chain()
    

    print(f"Blockchain valid after tampering: {blockchain.is_chain_valid()}")
    print(f"Hash in Block 2 still points to original Block 1 hash: {blockchain.chain[2].previous_hash}")