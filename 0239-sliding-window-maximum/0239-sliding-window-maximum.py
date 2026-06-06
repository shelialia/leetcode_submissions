from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # stores indexes
        left, right = 0, 0

        while right < len(nums):
            if q and left > q[0]:
                q.popleft()
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if (right + 1) >= k:
                left += 1
                res.append(nums[q[0]])
            
            right += 1
        return res


