"""
Name: Merge Two Sorted Lists (#21)  
URL: https://leetcode.com/problems/merge-two-sorted-lists/  

Time Complexity: O(N)  
Space Complexity: O(1)  
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else: 
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next
        
        temp.next = list1 if list1 else list2

        return dummy.next