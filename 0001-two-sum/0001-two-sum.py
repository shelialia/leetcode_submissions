from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[num] = i
        print(num_dict)
        for i, num in enumerate(nums):
            desired = target - num
            if desired in num_dict and num_dict[desired] > i:
                return [i, num_dict[desired]]