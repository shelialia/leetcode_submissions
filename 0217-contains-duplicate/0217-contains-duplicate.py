class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Use a set
        - insert/remove, check if in the set:
            - is O(1) on average case, but O(n) on worst case
        Time Complexity: O(n) as we loop through once
        - "in" check and add operation are O(1)
        Space Complexity: O(n) in worst case, all elements are distinct
        """
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False
        