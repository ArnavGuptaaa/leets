"""
Link : https://leetcode.com/discuss/post/6244752/google-l3-interview-experience-questions-2utz/

Question:
You are given a 0-indexed array nums of positive integers. You can start at any index in the array. 

At every position i, you have two choices:
    - Skip the current element and move to the next index (i + 1).
    - Take the current element:
        Add nums[i] to your score.
        Jump to index i + nums[i].

Your goal is to choose elements to maximize your score, under the constraint that after taking an element, you jump by its value. 
You cannot go out of bounds.

Return the maximum score achievable from any starting index.
"""

class Solution:
    def maximize_score(self, nums):
        cache = [-1] * len(nums)

        def dp(idx):
            if idx >= len(nums):
                return 0

            if cache[idx] != -1:
                return cache[idx]

            take = nums[idx] + dp(idx + nums[idx])
            leave = dp(idx + 1)

            cache[idx] = max(take, leave)
            return cache[idx]

        return dp(0)
        
# Tests
test_cases = [
    ([3, 4, 1, 2, 5, 6], 11) 
]
sol = Solution()
for i, (nums, expected) in enumerate(test_cases):
    result = sol.maximize_score(nums)
    print(f"Test {i}: {nums}| Expected: {expected} | Actual: {result} | {'PASS' if result == expected else 'FAIL'}")