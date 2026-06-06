from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        monatonically decreasing deque
        Why use a deque? 
        o(1) insert/delete at front AND back of queue
        Compared to a stack, whereby we are unable to efficiently access the "front of the stack"
        How it works:
        1. Deque stores indexes
        - Front is the index with largest value in the window
            - At each iteration, we check if front value is outdated; remove if it is.
        - Back is for us to add "possible largests in the window"
            - At each iteration, we compare our current value with the values at the back of the deque
            - While value of index at back of stack < curr value, they are "outdated possible max", so we pop them
            - Then, we add the index of our "new possible max value"
        2. Only append result when (right + 1) >= k because it's when the window starts to move
        3. Only if (right + 1) >= k then we move our left pointer too (window moves)
        4. At every iteration, we move our right pointer. 

        Time Complexity: O(n); The pop and append operations are amortized O(1) on average
        Space Complexity: O(n); Worst case where nums is strictly decreasing then every element is added to the queue AND the window size k == size of array nums
        """
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


