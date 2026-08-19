class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Counter array (s1) to store char -> count in whole s1
        # Counter array (s2) store char -> count in sliding window
        # permutations -> s1 can be in any order
        # keep advancing right pointer
        # while count in s2 does not match corresponding count in s1, shift left pointer
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for char in s1:
            s1_counter[ord(char) - ord("a")] += 1
        
        left = 0

        for right in range(len(s2)):
            # Add char
            s2_counter[ord(s2[right]) - ord("a")] += 1

            # If window too big, remove char
            if (right - left + 1) > len(s1):
                s2_counter[ord(s2[left]) - ord("a")] -= 1
                left += 1
            
            # Objective
            if s1_counter == s2_counter:
                return True
        return False