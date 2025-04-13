"""
Name: Happy Number (#202)
URL: https://leetcode.com/problems/happy-number/
"""

class Solution:
    def get_sum_of_squares(self, num):
        out = 0

        while num != 0:
            digit = num % 10
            out += digit ** 2

            num = num // 10
        
        return out
    
    """
    Time Complexity: O(Log N)
    Space Complexity: O(1)
    """
    def set_soln(self, num):
        seen = set()

        while num not in seen:
            if num == 1:
                return True

            seen.add(num)
            num = self.get_sum_of_squares(num)
        
        return False

    """
    Time Complexity: O(Log N)
    Space Complexity: O(1)
    """
    def linked_list_soln(self, num):
        slow = fast = num

        while True:
            slow = self.get_sum_of_squares(slow)
            fast = self.get_sum_of_squares(self.get_sum_of_squares(fast))

            if fast == slow:
                break

        return slow == 1

    def isHappy(self, num: int) -> bool:
        # return self.set_soln(num)
        return self.linked_list_soln(num)