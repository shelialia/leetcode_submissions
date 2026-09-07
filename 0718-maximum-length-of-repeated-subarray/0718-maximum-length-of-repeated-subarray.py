class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Let dp[i][j] = Longest subsuequence
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_len = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])
                    max_len = max(max_len, dp[i][j])
        return max_len
        
        