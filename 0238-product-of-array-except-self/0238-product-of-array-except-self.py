class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix_pdt = nums[0]
        for i in range(1, len(nums)):
            res[i] *= prefix_pdt
            prefix_pdt *= nums[i]

        postfix_pdt = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            res[j] *= postfix_pdt
            postfix_pdt *= nums[j]
        return res