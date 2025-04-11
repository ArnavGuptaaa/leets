"""
Name: Reorder List (#143)  
URL: https://leetcode.com/problems/reorder-list/  

Time Complexity: O(N)  
Space Complexity: O(1)  
"""

class Solution:
    def getMidNode(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverseLL(self, head):
        if not head:
            return 

        back = None
        curr = front = head

        while front.next:
            front = curr.next
            curr.next = back
            back = curr
            curr = front

        front.next = back

        return front
 
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return head

        midNode = self.getMidNode(head)

        secondHead = self.reverseLL(midNode.next)

        midNode.next = None
        
        resHead = head

        while secondHead:
            temp1 = head.next
            temp2 = secondHead.next

            head.next = secondHead
            secondHead.next = temp1

            head = temp1
            secondHead = temp2
        
        return resHead
        