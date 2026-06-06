class Solution:
    def search(self, rotatedArray: List[int], target: int) -> int:
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