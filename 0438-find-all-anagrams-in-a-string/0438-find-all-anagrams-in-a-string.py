from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        res = []
        char_dict_s = Counter()
        char_dict_p = Counter(p)

        for i, char in enumerate(s):
            char_dict_s[char] += 1

            if i >= len(p):
                char_dict_s[s[i - len(p)]] -= 1
            if char_dict_s == char_dict_p:
                res.append(i - len(p) + 1)
        return res
