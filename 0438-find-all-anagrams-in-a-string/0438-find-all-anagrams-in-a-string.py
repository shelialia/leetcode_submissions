from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        res = []
        char_dict_s = defaultdict(int)
        char_dict_p = defaultdict(int)

        for i in range(len(p)):
            char_dict_p[p[i]] += 1

        for i, s_char in enumerate(s):
            char_dict_s[s_char] += 1

            if i >= len(p):
                char_dict_s[s[i - len(p)]] -= 1
            if char_dict_s[s[i - len(p)]] == 0:
                char_dict_s.pop(s[i - len(p)])

            if char_dict_s == char_dict_p:
                res.append(i - len(p) + 1)
        return res
