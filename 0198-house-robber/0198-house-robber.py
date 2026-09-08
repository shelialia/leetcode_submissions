class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max(first + nums[i], second)
            first = second
            second = temp
        return second


"""
nums = [1,2,3,1]
Rob 1 + 3 = 4 (Output = 4)
Rob 2 + 1 = 3

nums = [2,7,9,3,1]
Rob 2 + 9 + 1 = 12 (Output = 12)
Rob 7 + 3 = 10

dp[i] = max amount you can rob from house 0..i

1. Rob house i:
   We cannot rob i-1, so:
   dp[i-2] + nums[i]

2. Skip house i:
   Best remains:
   dp[i-1]

Therefore:
dp[i] = max(dp[i-2] + nums[i], dp[i-1])
"""