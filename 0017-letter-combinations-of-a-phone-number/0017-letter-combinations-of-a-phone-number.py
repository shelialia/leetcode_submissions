class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []

        def dfs(index, path):
            # path is a string
            if index == len(digits):
                res.append("".join(path))
                return

            curr_digit = digits[index]
            possible_mapping = mapping[curr_digit]
            for pos in possible_mapping:
                path.append(pos)
                dfs(index + 1, path)
                path.pop()
                
        dfs(0, [])
        return res