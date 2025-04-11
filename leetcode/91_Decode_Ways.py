"""
Name: Decode Ways (#91)
URL: https://leetcode.com/problems/decode-ways/
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        """
        Time Complexity: O(N)
        Space Complexity: O(N + N)
        """
        def memo_ways(idx):
            if idx == len(s):
                return 1

            if idx in cache:
                return cache[idx]
            
            if s[idx] == '0':
                return 0

            res = ways(idx + 1)

            if (
                idx + 1 < len(s) and 
                (
                    s[idx] == '1' or
                    (
                        s[idx] == '2' and
                        s[idx + 1] in '0123456'
                    )
                )
            ):
                res += ways(idx + 2)

            cache[idx] = res

            return res


        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        def tab_ways():
            cache[len(s)] = 1

            for idx in range(len(s) - 1, -1, -1):
                if s[idx] == "0":
                    cache[idx] = 0
                    continue

                cache[idx] = cache[idx + 1]

                if (
                    idx + 1 < len(s) and 
                    (
                        s[idx] == '1' or
                        (
                            s[idx] == '2' and
                            s[idx + 1] in '0123456'
                        )
                    )
                ):
                    cache[idx] += cache[idx + 2]

            return cache[0]
        
        # Memoized
        return memo_ways(0)

        # Tabulated
        return tab_ways()