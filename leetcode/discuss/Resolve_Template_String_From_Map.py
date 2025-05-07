"""
Link : https://leetcode.com/discuss/post/6049364/googlel4phone-screen-round-by-anonymous_-bonl/

Question:
You are given a dictionary template_map where each key maps to a string value. 
The value itself may contain other keys from the map in the form of template variables, denoted as "%KEY%".
You are also given a string input_template that may contain such template variables.

Your task is to resolve the input string by recursively replacing all variables using the given map until no template variables remain.
"""

"""
NOTE: 
- This solution doesnt handle cyclic dependency. in order to handle that, We need to add a visited set.
- We are doing redundant work of recalculating the keys everytime. Just memo them.
"""

class Solution:
    def get_resolved_string(self, template_string, template_map):
        stack = []

        idx = 0
        while idx < len(template_string):

            if template_string[idx] != '%':
                stack.append(template_string[idx])

            else:
                key = ''
                resolved_string = ''

                idx += 1
                while template_string[idx] != '%':
                    key += template_string[idx]

                    idx += 1

                if key in template_map:
                    resolved_string = self.get_resolved_string(template_map[key], template_map)
                else:
                    resolved_string = f'%{key}%'
                
                stack.append(resolved_string)

            idx += 1

        return "".join(stack)


# Tests

# Test
sol = Solution()
test_cases = [
    # Simple direct replacement
    ["%X%", {"X": "123"}, "123"],

    # Nested replacement
    ["%X%_%Y%", {"X": "123", "Y": "456_%X%"}, "123_456_123"],

    # Multiple nested placeholders
    ["%A%_%B%_%C%", {"A": "%B%", "B": "%C%", "C": "Z"}, "Z_Z_Z"],

    # No placeholders in string
    ["static_text", {"X": "123"}, "static_text"],

    # Placeholder with empty value
    ["%X%_%Y%", {"X": "", "Y": "YAY"}, "_YAY"],

    # Multiple instances of same placeholder
    ["%X%_%X%_%X%", {"X": "repeat"}, "repeat_repeat_repeat"],

    # Placeholder in map value not used in template string
    ["%A%", {"A": "A_val", "B": "B_val_%A%"}, "A_val"],

    # Placeholder value references another placeholder, which is empty
    ["%A%", {"A": "%B%", "B": ""}, ""],

    # Value with adjacent placeholders
    ["%A%%B%", {"A": "hello", "B": "world"}, "helloworld"],

    # Deep nested chain
    ["%A%", {"A": "%B%", "B": "%C%", "C": "%D%", "D": "end"}, "end"],
]

for idx, case in enumerate(test_cases):
    template_string, template_map, expected = case

    result = sol.get_resolved_string(template_string, template_map)
    print(f'{idx + 1}. | Expected : {expected} | Actual : {result} | {'PASS' if expected == result else 'FAIL'}')