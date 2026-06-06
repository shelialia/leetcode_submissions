class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. Sort the array
        2. Create list to track the unique triplets (cannot be repeated)
        3. Iterate through nums:
        - If same as previous value, skip (will get duplicate triplet)
        - Performance enhancement: if num>0, there's no way to get sum 0
        - 2 Pointer solution (since the array is sorted) to get the 2 indexes
            - if target is found, we skip the duplicates on left & right
        """
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if num > 0: # if num>0, there's no way to get sum 0
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