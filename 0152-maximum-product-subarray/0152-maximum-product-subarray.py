class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = nums[0]
        curr_max = nums[0]
        res = nums[0]

        # Include nums[i] itself because we may want to start a new subarray at i instead of extending the previous one.
        for i in range(1, len(nums)):
            prev_min = curr_min
            prev_max = curr_max

            curr_min = min(
                nums[i],
                prev_min * nums[i],
                prev_max * nums[i]
            )
            curr_max = max(
                nums[i],
                prev_min * nums[i],
                prev_max * nums[i]
            )
            res = max(res, curr_max)
        return res

"""
nums = [2,3,-2,4]
            ^
min_pdt = -48
max_pdt = 6

Naive:
Generate all O(n²) subarrays.
If recalculating each product from scratch:
Time: O(n³)

DP idea:

Because multiplying by a negative number can swap the maximum and minimum,
we must track both.

max_dp[i] = maximum product of a subarray ending at i
min_dp[i] = minimum product of a subarray ending at i

For nums[i]:

max_dp[i] = max(
    nums[i],
    max_dp[i-1] * nums[i],
    min_dp[i-1] * nums[i]
)

min_dp[i] = min(
    nums[i],
    max_dp[i-1] * nums[i],
    min_dp[i-1] * nums[i]
)

Take the maximum max_dp[i] over all i.

Time: O(n)
Space: O(1) if only previous max/min are stored
"""
