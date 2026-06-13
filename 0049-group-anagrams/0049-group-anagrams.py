from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap of str -> list of anagrams
        freq_to_str = defaultdict(list)

        # Loop through strings
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord("a")] += 1
            freq_to_str[tuple(freq)].append(string)
        return list(freq_to_str.values())