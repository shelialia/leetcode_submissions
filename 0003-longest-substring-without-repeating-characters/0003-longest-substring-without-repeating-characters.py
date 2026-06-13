class Solution:
    # sliding window method
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest_len = 0
        left = 0

        for right in range(len(s)):
            while left < right and s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            # print("char_set", char_set)
            
            longest_len = max(longest_len, right - left + 1)

        return longest_len