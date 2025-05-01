"""
Link: https://leetcode.com/discuss/post/6701582/google-interview-l4-interview-by-anonymo-o79u/

Question : Design a custom Deque (including all deque methods) only using a hashMap.
"""

# Hashmap Solution
class CustomDeque:
    def __init__(self):
        self.front = -1
        self.back = -1
        self.deque_dict = {}

    def add_front(self, value):
        self.front -= 1
        self.deque_dict[self.front] = value
    
    def add_back(self, value):
        self.deque_dict[self.back] = value
        self.back += 1

    def remove_front(self):
        if self.is_empty():
            print('Queue Empty')

            return

        del self.deque_dict[self.front]
        self.front += 1

    def remove_back(self):
        if self.is_empty():
            print('Queue Empty')

            return

        self.back -= 1
        del self.deque_dict[self.back]
    
    def peek_front(self):
        if self.is_empty():
            print('Queue Empty')

            return

        return self.deque_dict[self.front]
    
    def peek_back(self):
        if self.is_empty():
            print('Queue Empty')

            return

        return self.deque_dict[self.back - 1]
    
    def is_empty(self):
        return len(self.deque_dict) == 0


# ====
# Linked List Solution
class ListNode:
    def __init__(self, value):
        self.val = value
        self.back = None
        self.next = None

class CustomDeque:
    def __init__(self):
        self.front = None
        self.tail = None
        self.size = 0

    def add_front(self, value):
        new_node = ListNode(value)
        self.size += 1

        if self is_empty():
            self.front = self.tail = new_node
            return
        
        new_node.next = self.front
        self.front.back = new_node

        self.front = new_node
    
    def add_back(self, value):
        new_node = ListNode(value)
        self.size += 1

        if self is_empty():
            self.front = self.tail = new_node
            return
        
        new_node.back = self.tail
        self.tail.next = new_node

        self.tail = new_node

    def remove_front(self):
        if self.is_empty():
            print('Queue Empty')

            return

        if self.front == self.tail:
            self.front = self.tail = None
        
        else:
            self.front = self.front.next
            self.front.back = None

        self.size -= 1


    def remove_back(self):
        if self.is_empty():
            print('Queue Empty')

            return

        if self.front == self.tail:
            self.front = self.tail = None
        
        else:
            self.tail = self.tail.back
            self.tail.next = None

        self.size -= 1
    
    def peek_front(self):
        if self.is_empty():
            print('Queue Empty')

            return

        return self.front.val
    
    def peek_back(self):
        if self.is_empty():
            print('Queue Empty')

            return

        return self.tail.val
    
    def is_empty(self):
        return self.size == 0