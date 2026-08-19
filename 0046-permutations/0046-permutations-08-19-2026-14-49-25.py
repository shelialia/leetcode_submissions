class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue
                path.append(num)
                used.add(num)

                backtrack(path)

                path.pop()
                used.remove(num)

        backtrack([])
        return res
