"""
Link : https://leetcode.com/discuss/post/5604226/google-phone-screen-l4-interview-by-anon-4a4f/

Question:
Given a sorted list of lowercase strings words and a string prefix, return the number of words in the list that start with the given prefix.
"""

class Solution:
    def search_string(self, strings, prefix, find_start):
        left = 0
        right = len(strings) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if len(strings[mid]) >= len(prefix) and strings[mid][:len(prefix)] == prefix:
                result = mid

                if find_start:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                end_idx = min(len(prefix), len(strings[mid]))

                if strings[mid][:end_idx] < prefix:
                    left = mid + 1
                else:
                    right = mid - 1

        return result

    def get_strings_with_same_prefix(self, strings, prefix):

        first_index = self.search_string(strings, prefix, True)
        last_index = self.search_string(strings, prefix, False)

        if first_index == -1:
            return 0

        return last_index - first_index + 1

# Test
sol = Solution()
test_cases = [
    # Base test case
    [["bomb", "book", "g","gift", "go", "goal", "goat", "gum","xray","yellow","zebra"], "go", 3],

    # Prefix matches nothing
    [["apple", "banana", "carrot"], "dog", 0],

    # Prefix matches everything
    [["apple", "applet", "application"], "app", 3],

    # Empty prefix (should match all)
    [["a", "ab", "abc", "abcd"], "", 4],

    # Empty word list
    [[], "test", 0],

    # Words shorter than prefix
    [["a", "b", "c", "de"], "dog", 0],

    # Prefix longer than any word
    [["cat", "car", "cart"], "cartoon", 0],

    # Mixed short and long
    [["do", "dog", "dogma", "doll", "dolphin"], "dog", 2],

    # Exact match
    [["a", "ab", "abc"], "abc", 1],
]

for idx, case in enumerate(test_cases):
    strings, prefix, expected = case

    result = sol.get_strings_with_same_prefix(strings, prefix)
    print(f'{idx + 1}. | Expected : {expected} | Actual : {result} | {'PASS' if expected == result else 'FAIL'}')