from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        monatonically decreasing deque
        Why use a deque? We want to have these features
        1. Insert at back of queue
        2. Pop from front of queue
        => Queue features so far
        3. Pop at the back of the queue => not allowed in queue structure
        - queues only allow to pop from the front
        => use a deque which allow us to pop/append from both front and back of queue
        
        How it works: Maintain a monatonically decreasing queue
        1. Deque stores indexes
        - Front is the index with largest value in the window
            - At each iteration, we check if front value is outdated; remove if it is.
        - Back is for us to add "possible largests in the window"
            - At each iteration, we compare our current value with the values at the back of the deque
            - While value of index at back of stack < curr value, they are "outdated possible max", so we pop them
            - Then, we add the index of our "new possible max value"
        2. Only append result when (right + 1) >= k because it's when window size hits k
        3. Only if (right + 1) >= k then we increment our left pointer too (window moves)
        4. At every iteration, we increment our right pointer. 

        Time Complexity: O(n); The pop and append operations are amortized O(1) on average
        Space Complexity: O(n); Worst case where nums is strictly decreasing then every element is added to the queue AND the window size k == size of array nums
        """
        queue = deque() # Monatonically decreasing queue storing indexes corresponding to the value
        res = []

        left = 0
        for right in range(len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            
            if (right + 1) >= k:
                res.append(nums[queue[0]])
                if queue[0] == left:
                    queue.popleft()
                left += 1
        return res
            
        