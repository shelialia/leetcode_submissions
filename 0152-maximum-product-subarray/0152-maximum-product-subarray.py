class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                res = max(res, 0)
                curMin, curMax = 1, 1
                continue
            tmp = curMin * n
            curMin = min(curMin * n, curMax * n, n)
            curMax = max(tmp, curMax * n, n)
            res = max(curMax, res)
        return res
