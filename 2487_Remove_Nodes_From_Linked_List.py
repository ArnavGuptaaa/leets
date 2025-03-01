"""
Name: Remove Nodes From Linked List (#2487)
URL: https://leetcode.com/problems/remove-nodes-from-linked-list/

Stack
Time Complexity: O(N)
Space Complexity: O(N)

LL Traversal
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def stackSolution(self, head):
        if not head:
            return None
        
        stack = [head.val]

        head = head.next

        while head:
            while len(stack) > 0 and stack[-1] < head.val:
                stack.pop()
                
            stack.append(head.val)
            head = head.next

        head = temp = ListNode(-1)

        for val in stack:
            temp.next = ListNode(val)
            temp = temp.next
        
        return head.next

    def traversalSolution(self, head):
        if not head:
            return None

        def reverseLL(head):
            back = None
            curr = front = head

            while curr:
                front = curr.next
                curr.next = back

                back = curr
                curr = front 

            return back 
        
        head = reverseLL(head)

        maxSoFar = head.val
        temp = head

        while temp and temp.next:
            if temp.next.val < maxSoFar:
                temp.next = temp.next.next
            else:
                maxSoFar = temp.next.val
                temp = temp.next

        return reverseLL(head)

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.stackSolution(head)
        return self.traversalSolution(head)