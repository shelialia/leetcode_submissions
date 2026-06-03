class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            desired = target - num
            if desired in num_dict:
                return [i, num_dict[desired]]
            else:
                num_dict[num] = i