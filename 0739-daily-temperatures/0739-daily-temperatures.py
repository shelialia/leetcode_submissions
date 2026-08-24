class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Use a stack to store (temp, index)
        - index allows us to calculate the number of days to wait
        - temp allows us to do the check for a warmer day
        Loop through temperatures.
        while stack[-1][0] < curr_temp:
            - res[stack[-1][1]] = curr_index - stack[-1][1]
        return res
        """
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, curr_i = stack.pop()
                res[curr_i] = i - curr_i
            stack.append((temp, i))
        return res

