class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr_char_set = [0] * 26
        longest_len = 0
        left = 0

        for right in range(len(s)):
            curr_char_set[ord(s[right]) - ord("A")] += 1

            while (right - left + 1) - max(curr_char_set) > k:
                curr_char_set[ord(s[left]) - ord("A")] -= 1
                left += 1
            longest_len = max(longest_len, right - left + 1)
            
        return longest_len