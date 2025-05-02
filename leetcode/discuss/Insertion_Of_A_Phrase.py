"""
Link : https://leetcode.com/discuss/post/6386506/google-l3-phone-screen-by-anonymous_user-gjax/

Question :

Given two strings s1 and s2, find out if they only differ by the insertion of a phrase.

Example #1:
The boy goes to the hospital
The cute little boy goes to the hospital
'cute litte' is the added phrase everything else is the same so return True

Example #2:
The boy is nice.
The girl is nice.
-> Return False
"""


class Solution:
    def __init__(self):
        pass
    
    def check_insertion(self, s1, s2):
        if len(s1) == len(s2):
            return False

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        if len(s1.strip()) == 0:
            return True
        
        words_s1 = s1.split(' ')
        words_s2 = s2.split(' ')

        prefix = 0
        for idx, word in enumerate(words_s2):
            if idx >= len(words_s1):
                break

            if word != words_s1[idx]:
                break

            prefix += 1

        
        suffix = 0
        for idx, word in enumerate(reversed(words_s2)):
            if idx >= len(words_s1):
                break 

            end_idx = -1 - idx

            if word != words_s1[end_idx]:
                break

            suffix += 1

        print(prefix, suffix, words_s1)
        return prefix + suffix == len(words_s1)


# Test
sol = Solution()

test_cases = [
    ["the boy goes to the hospital", "the cute little boy goes to the hospital", True],
	["the boy is nice", "the girl is nice", False],
	["he loves apples", "sometimes he loves apples", True],
	["we are here", "we are here for you", True],
	["dogs bark loud", "dogs really loud bark", False],
	["I eat food", "I food eat healthy", False],
	["life is good", "life sometimes unexpectedly is good", True],
	["she likes to swim", "she to swim", True],
	["go to school", "go quickly to high school", False],
	["stay strong", "stay strong", False],
	["a b c", "a b d c b", False],
    ["ABC", "", True]
]

for s1, s2, expected in test_cases:
    actual = sol.check_insertion(s1, s2)

    print('===')
    print(f'{s1}\n{s2}\nExpected: {expected}, Actual: {actual}')
    print('===\n')