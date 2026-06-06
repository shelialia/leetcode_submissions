class Solution:
    def search(self, rotatedArray: List[int], target: int) -> int:
        """
        Binary search spin off qn

        Foundations of qn:
        1. Condition on left <= right
        2. if medvalue == target: return the index
        3. Else, find out which half of the array the medpoint is in
        - Left half of array: if medvalue > leftmost value
            > Search leftside of med: if target between left and med
            > Search rightside of med: if target is not
        - Right half of array: if medvalue < rightmost value
            > Search rightside of med: if target between med and right
            > Search leftside of med: if target is not
        4. Else, return -1 (value not found)

        Time complexity: O(n); 2 pointer through the array
        Space complexity: O(1); no extra space used
        """
        left, right = 0, len(rotatedArray) - 1

        while left <= right:
            med = (left + right) // 2

            if rotatedArray[med] == target:
                return med
            # compare against the last elem
            # first half: larger than last elem
            # second half: smaller than last elem
            if rotatedArray[med] < rotatedArray[right]: # med in second half
                if rotatedArray[med] < target <= rotatedArray[right]:
                    left = med + 1
                else:
                    right = med - 1
            else:
                if rotatedArray[left] <= target < rotatedArray[med]:
                    right = med - 1
                else:
                    left = med + 1
        return -1