"""
Name: Count the Hidden Sequences (#2145)
URL: https://leetcode.com/problems/count-the-hidden-sequences/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        running_sum = 0
        mini = 0
        maxi = 0

        for diff in differences:
            running_sum += diff
            
            mini = min(mini, running_sum)
            maxi = max(maxi, running_sum)

        difference_range = maxi - mini
        allowed_range = upper - lower

        if difference_range > allowed_range:
            return 0

        return allowed_range - difference_range + 1


"""
[3,-4,5,1,-2]

pretend we start with x as the first number
hidden[0] = x
hidden[1] = x + 3
hidden[2] = x + 3 - 4
hidden[3] = x + 3 - 4 + 5
...

Can also be expressed as
hidden[0] = x
hidden[1] = x + prefix[0]
hidden[2] = x + prefix[1]
hidden[3] = x + prefix[2]
...

General formula:
hidden[idx] = x + prefix[idx - 1]

Since we are dealing with a range, we want to find min and max values for hidden[idx]

max(hidden[idx]) = x + max(prefix[idx - 1])
min(hidden[idx]) = x + min(prefix[idx - 1])

subtract both

range = max - min = max(prefix[idx - 1]) - min(prefix[idx - 1])

now, if the range of this functions is greater than given range (upper - lower), then we return 0
else, 
    we subtract the ranges to yield how many of such shifts can be made with the function range
"""