class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Basically the inner loop of 3Sum solution
        """
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return [left + 1, right + 1]
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1