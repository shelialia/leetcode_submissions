class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Counter array with length 26 storing the counts of each english char
        # Sliding window problem
        # While k < len(window) - max(highest occurrence in window) 
        # chars that need replacement == len(window) - max(highest occurrence in window) 
        # shift left pointer. otherwise, can continue expanding window to right
        counter = [0] * 26
        max_len = 0
        left = 0
        for right in range(len(s)):
            counter[ord(s[right]) - ord("A")] += 1
            while k < (right - left + 1) - max(counter):
                counter[ord(s[left]) - ord("A")] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
