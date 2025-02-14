"""
Name: Add Two Numbers (#2)  
URL: https://leetcode.com/problems/add-two-numbers/  

Time Complexity: O(N)  
Space Complexity: O(N)  
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False

        temp1 = l1
        temp2 = l2

        while temp1 or temp2:
            
            digit1 = temp1.val if temp1 else 0
            digit2 = temp2.val if temp2 else 0


            nodeSum = digit1 + digit2 + 1 if carry else digit1 + digit2
            carry = nodeSum >= 10

            temp1.val = nodeSum % 10
            
            # If next node on temp1 does not exist
            # but next node exists on temp2, or theres a carry
            # then create a new node on temp1
            if ((not temp1.next) and ((temp2 and temp2.next) or carry)): 
                temp1.next = ListNode(0)

            temp1 = temp1.next
            temp2 = temp2.next if temp2 else temp2
            
        return l1