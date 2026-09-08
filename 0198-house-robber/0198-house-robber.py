class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return max(dp[-1], dp[-2])


"""
nums = [1,2,3,1]
Rob 1 + 3 = 4 (Output = 4)
Rob 2 + 1 = 3

nums = [2,7,9,3,1]
Rob 2 + 9 + 1 = 12 (Output = 12)
Rob 7 + 3 = 10

dp[i] = max amount you can rob
dp[i] = max(rob i - 2 house + i house, rob i - 1 house + skip i house)
dp[i] = max(dp[i - 2] + num[i], dp[i - 1])
"""