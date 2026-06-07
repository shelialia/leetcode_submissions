from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        If allowed, use Counter. 
        Else, use defaultdict but must rmb to pop a key when its value (ie. count) == 0
        - 2 defaultdicts where 1 has extra keys with count 0 are NOT the same
        
        How to solve?
        1. Create defaultdict for both s and p
        2. Count number of each char in p
        3. Iterate through s: "Sliding window of size len(p) through s
        - See new char, add to s's defaultdict
        - If at least length of p, remove old char (keep window at size 
        of len(p) and update defaultdict)
        - Check of 2 dd are the same; if yes, append leftmost index of window to the result
        """
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
