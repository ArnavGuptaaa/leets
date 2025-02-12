"""
Name: Reverse Linked List (#206)  
URL: https://leetcode.com/problems/reverse-linked-list/  

Time Complexity: O(N)  
Space Complexity: O(1)  
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        if not head.next: 
            return head 
            
        back = None
        curr = front = head

        while front.next:
            front = curr.next
            curr.next = back

            back = curr
            curr = front

        front.next = back

        return front