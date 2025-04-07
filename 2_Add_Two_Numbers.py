"""
Name: Add Two Numbers (#2)  
URL: https://leetcode.com/problems/add-two-numbers/  

Time Complexity: O(N)  
Space Complexity: O(N)  
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        temp = dummy

        carry = 0
        while l1 or l2 or carry:

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            add = (num1 + num2 + carry) % 10
            carry = (num1 + num2 + carry) // 10

            new_node = ListNode(add)
            temp.next = new_node
            temp = temp.next
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return dummy.next