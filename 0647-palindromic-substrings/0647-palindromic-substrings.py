class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(start, end) -> int:
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                print(start, end)
                start -= 1
                end += 1
                count += 1
            return count
        res = 0
        for i in range(len(s)):
            res += expand(i, i)
        
        for j in range(len(s) - 1):
            res += expand(j, j + 1)
        return res

"""
Naive:
Generate O(n²) substrings.
Check whether each substring is a palindrome in O(n).
Time: O(n³)
Space: O(1) ignoring substring creation

Expand from center:
There are O(n) possible centers.
Each center can expand O(n) times.
- Account for even and odd substring, call helper function twice
Time: O(n²)
Space: O(1)

DP:
dp[i][j] = whether s[i...j] is a palindrome

dp[i][j] =
    s[i] == s[j]
    AND
    (length <= 2 OR dp[i+1][j-1])

There are O(n²) states.
Each state takes O(1) work.

Time: O(n²)
Space: O(n²)
"""