"""
Name: Linked List Cycle (#141)  
URL: https://leetcode.com/problems/linked-list-cycle

Time Complexity: O(N)  
Space Complexity: O(1)  
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fastPointer = head 
        slowPointer = head 
        
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:
                return True
        
        return False