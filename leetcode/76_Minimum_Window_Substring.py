"""
Name: Minimum Window Substring (#76)
URL: https://leetcode.com/problems/minimum-window-substring/

Time Complexity: O(S + T)
Space Complexity: O(S + T)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        if len(s) < len(t):
            return ""

        # Calculate frequency of t
        freq_t = {}

        for ch in t:
            if ch not in freq_t:
                freq_t[ch] = 0

            freq_t[ch] += 1

        # Setup window
        have, need = 0, len(freq_t)
        left = right = 0
        window_freq = {}
        result_indexes = [-1, -1]
        result_length = float('inf')

        for right in range(len(s)):
            ch = s[right]

            if ch not in window_freq:
                window_freq[ch] = 0

            window_freq[ch] += 1

            if ch in freq_t and window_freq[ch] == freq_t[ch]:
                have += 1
            
            # If window has all elements, shrink from left to find minimum window
            while have == need:
                if (right - left + 1) < result_length:
                    result_length = right - left + 1
                    result_indexes = [left, right]

                if s[left] in freq_t and window_freq[s[left]] == freq_t[s[left]]:
                    have -= 1

                window_freq[s[left]] -= 1
                left += 1

        return s[result_indexes[0] : result_indexes[1] + 1] if result_length != float('inf') else ""