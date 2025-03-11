"""
Name: Merge k Sorted Lists (#23)
URL: https://leetcode.com/problems/merge-k-sorted-lists/

Time Complexity: O(Nk)
Space Complexity: O(1)
"""

class Solution:
    # Merges two sorted lists into one
    def merge2Lists(self, head1, head2):
        temp1 = head1
        temp2 = head2

        resDummy = ListNode(0)
        resTemp = resDummy

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                resTemp.next = temp1
                temp1 = temp1.next
            else: 
                resTemp.next = temp2
                temp2 = temp2.next
            
            resTemp = resTemp.next
        
        if temp1:
            resTemp.next = temp1
        
        if temp2:
            resTemp.next = temp2

        return resDummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        listLen = len(lists)

        if listLen == 0:
            return None 
            
        if listLen == 1:
            return lists[0]
        
        mergedListHead = self.merge2Lists(lists[0], lists[1])
        
        idx = 2

        while idx < listLen:
            mergedListHead = self.merge2Lists(mergedListHead, lists[idx])
            idx += 1

        return mergedListHead


"""
Name: Merge k Sorted Lists (#23)
URL: https://leetcode.com/problems/merge-k-sorted-lists/

Time Complexity: O(N LogK) [K: Length of lists]
Space Complexity: O(K) [K: Length of lists]
"""

# Heap Solution
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # O(K) [K: Length of lists]
        for idx, node in enumerate(lists):
            if node:
                # O(LogK) [K: Length of lists]
                heapq.heappush(min_heap, (node.val, (idx, node)))

        dummy = ListNode(-1)
        temp = dummy

        # O(N)
        while min_heap:
            _, (idx, node) = heapq.heappop(min_heap)

            temp.next = node
            temp = temp.next

            if node.next:
                # O(LogK) [K: Length of lists]
                heapq.heappush(min_heap, (node.next.val, (idx, node.next)))

        return dummy.next