"""
Name: Remove Nth Node From End of List (#19)  
URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/  

Time Complexity: O(N)  
Space Complexity: O(1)  
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = front = head
        back = None

        for i in range(n-1):
            front = front.next

        while front.next:
            back = curr
            curr = curr.next
            front = front.next

        if not back:
            head = curr.next
            curr.next = None
            return head

        back.next = curr.next
        curr.next = None

        return head