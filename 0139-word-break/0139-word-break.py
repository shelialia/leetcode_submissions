class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for word in wordDict:
                word_len = len(word)
                if (i - word_len) >= 0 and s[i - word_len: i] == word and dp[i - word_len]:
                    dp[i] = True
        return dp[-1]

"""
s = "leetcode", wordDict = ["leet","code"]
Output = True

dp[i] == whether s[:i] can be segmented into space-separated sequence of 1 or more dictionary words

Rough logic
for i, char in s
    for word in wordDict
        # do index checking here
        if s[i - len(word):i] == word and dp[i - len(word)] 
            dp[i] = True
return dp[-1]

n = len(s)
m = len(wordDict)
Time complexity: O(nm)
- nested loop: O(nm)

Space complexity: O(n)
"""