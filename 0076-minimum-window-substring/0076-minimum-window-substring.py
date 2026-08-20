from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Brute force method -> generate all substrings, then compare the substring with t by creating a hashmap for each and checking if the char in substring >= chars in t. 
        # O(n^3) time => O(n^2) to generate substring and for each substring, O(n) time to compare

        # Sliding window method
        # keep track of target # matches == len(t)
        # keep track of matches in current window for s
        # keep adding new chars by advancing right pointer.
        # - if adding a new char leads to a character count match between substring and t, increment match
        # - when matches == target, we found a possible substring.
        #      - add to result
        #      - while matches == target, advance left pointer. If removing a char leads to a character count mismatch between substring and t, decrement match
        counter_t = Counter(t) # -> O(m) 
        counter_window = defaultdict(int)
        target = len(counter_t)
        matches = 0

        min_window = (float("inf"), 0, 0)
        left = 0
        # O(n) time
        for right in range(len(s)):
            counter_window[s[right]] += 1
            if s[right] in counter_t and counter_window[s[right]] == counter_t[s[right]]:
                substring = []
                matches += 1
            while matches == target:
                if (right - left + 1) < min_window[0]:
                    min_window = (right - left + 1, left, right)
    
                if s[left] in counter_t and counter_window[s[left]] == counter_t[s[left]]:
                    matches -= 1
                counter_window[s[left]] -= 1
                left += 1
        return s[min_window[1]:min_window[2] + 1] if min_window[0] != float("inf") else ""
