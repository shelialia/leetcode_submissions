class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        "Sliding window" problem
        Keep track of the currSum (prefix sum before the index)
        If the currSum is negative, discard it (reset)
        - because it would not help the case
        Otherwise, it is possibly helpful (get a bigger sum)
        - Add it!
        Time complexity: O(n) - a single loop
        Space complexity: O(1) - no extra space used
        """
        maxSum = nums[0]
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum
        

