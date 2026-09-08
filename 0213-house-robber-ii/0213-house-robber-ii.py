class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def house_robber(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                temp = max(first + nums[i], second)
                first = second
                second = temp
            return second
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))

"""
nums = [2,3,2]
can only rob house 1 OR house 3
output = 2 (house 1 or house 3)
output = 3 <<< chosen

nums = [1,2,3,1]
can only rob house 1 or house 4
output = 1 + 3 = 4 <<<< chosen!!
output = 2 + 1 = 3

dp1[i] = max amount you can rob from 0..i exclude final index
dp2[i] = max amount you can rob from 1..i (exclude first index)

dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
"""