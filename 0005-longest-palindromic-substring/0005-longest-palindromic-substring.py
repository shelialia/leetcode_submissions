class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        max_len = 0
        res = s[0]
        dp = [[False] * n for _ in range(n)]
        # dp[i][j] = True if s[i:j + 1] is a palindrome

        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if s[start] == s[end]:
                    if length == 2 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if length > max_len:
                            max_len = length
                            res = s[start: end + 1]
        return res

"""
s = "babad"
Output = "bab" or "aba"

s = "cbbd"
Output = "bb"

Naive:
Generate O(n^2) substrings.
Checking each substring takes O(n).
Total Time = O(n^3)

DP:
dp[i][j] = whether substring s[i...j] is a palindrome

A substring is a palindrome if:
- s[i] == s[j]
- the inner substring s[i+1...j-1] is also a palindrome

dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

Base cases:
- length 1 => palindrome
- length 2 => palindrome if both characters are equal

Time: O(n^2)
Space: O(n^2)
"""

