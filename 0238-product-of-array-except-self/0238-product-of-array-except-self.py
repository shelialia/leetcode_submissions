class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        curr_pdt = nums[0]
        for i in range(1, len(nums)):
            print(curr_pdt)
            res[i] *= curr_pdt
            curr_pdt *= nums[i]
        back_pdt = nums[len(nums) - 1]
        for j in range(len(nums) - 2,-1, -1):
            res[j] *= back_pdt
            back_pdt *= nums[j]
        return res