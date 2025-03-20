"""
Name: Hand of Straights (#846)
URL: <Add question link here>

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Return false, If cards cant be evenly distributed, 
        if len(hand) % groupSize != 0:
            return False
        
        # Prepare all card frequencies
        freq_map = {}

        for card in hand:
            freq_map[card] = freq_map.get(card, 0) + 1

        sorted_keys = sorted(freq_map.keys())

        # Iterate over cards in a sorted fashion
        # Ex => if we have cards as [3,2,1], we will lock 3 and look for 3,4,5 group (size 3)
        #       If we have them as [1,2,3], we will lock 1 and look for 1,2,3
        for idx, card in enumerate(sorted_keys):
            if freq_map[card] == 0:
                continue

            freq = freq_map[card]
            for d_idx in range(groupSize):
                # If start card has greater occourances than consecutive ones,
                # Then it will never be fully used
                if freq > freq_map.get(sorted_keys[idx] + d_idx, 0):
                    return False

                # Consume all cards
                freq_map[sorted_keys[idx] + d_idx] -= freq

        return True