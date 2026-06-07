from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(s + t) because Counter(string) takes O(n) time to build
        Space Complexity: O(s + t) because worst case s and t contain unique characters
        """
        return Counter(s) == Counter(t)
