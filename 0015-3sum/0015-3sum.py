class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        """
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if num > 0:
                break
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else: # cur_sum == 0
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res