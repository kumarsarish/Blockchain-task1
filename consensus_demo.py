import random
from typing import Dict, List, Any
from collections import Counter

class ConsensusDemo:
    """Demonstration of different blockchain consensus mechanisms."""
    
    @staticmethod
    def proof_of_work() -> Dict[str, Any]:
        """Simulate Proof of Work (PoW) consensus.
        
        Returns:
            Dict: Contains winner name and their computational power
        """
        miners = {
            'Alice': random.randint(1, 100),
            'Bob': random.randint(1, 100),
            'Carol': random.randint(1, 100)  
        }
        winner = max(miners, key=miners.get)
        return {
            'mechanism': 'PoW',
            'participants': miners,
            'winner': winner,
            'score': miners[winner],
            'metric': 'computational power'
        }
    
    @staticmethod
    def proof_of_stake() -> Dict[str, Any]:
        """Simulate Proof of Stake (PoS) consensus.
        
        Returns:
            Dict: Contains winner name and their stake amount
        """
        stakers = {
            'Charlie': random.randint(1, 100),
            'Dave': random.randint(1, 100),
            'Eve': random.randint(1, 100) 
        }
        winner = max(stakers, key=stakers.get)
        return {
            'mechanism': 'PoS',
            'participants': stakers,
            'winner': winner,
            'score': stakers[winner],
            'metric': 'stake amount'
        }
    
    @staticmethod
    def delegated_proof_of_stake(num_voters: int = 10) -> Dict[str, Any]:
        """Simulate Delegated Proof of Stake (DPoS) consensus.
        
        Args:
            num_voters: Number of voters in the system
            
        Returns:
            Dict: Contains election results and vote distribution
        """
        delegates = ['Frank', 'Grace', 'Heidi', 'Ivan']  
        votes = random.choices(
            delegates,
            weights=[40, 30, 20, 10],  
            k=num_voters
        )
        vote_counts = Counter(votes)
        winner = max(vote_counts, key=vote_counts.get)
        
        return {
            'mechanism': 'DPoS',
            'delegates': delegates,
            'votes': votes,
            'vote_counts': dict(vote_counts),
            'winner': winner,
            'score': vote_counts[winner],
            'metric': 'votes received',
            'total_voters': num_voters
        }
    
    @classmethod
    def run_demo(cls):
        """Run complete consensus mechanisms demonstration."""
        print("BLOCKCHAIN CONSENSUS MECHANISMS DEMO\n")
        
        
        pow_result = cls.proof_of_work()
        pos_result = cls.proof_of_stake()
        dpos_result = cls.delegated_proof_of_stake()
        
        
        for result in [pow_result, pos_result, dpos_result]:
            print(f"[{result['mechanism']}]")
            print(f"Participants: {result.get('participants', result.get('delegates'))}")
            
            if result['mechanism'] == 'DPoS':
                print(f"Vote distribution: {result['vote_counts']}")
                print(f"Total voters: {result['total_voters']}")
            else:
                for name, score in result['participants'].items():
                    print(f"{name}: {score} {result['metric']}")
            
            print(f"Winner: {result['winner']} ({result['score']} {result['metric']})\n")

if __name__ == "__main__":
    random.seed(42) 
    ConsensusDemo.run_demo()