class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(str):
            start, end = 0, len(str) - 1
            while start <= end:
                if str[start] != str[end]:
                    return False
                start += 1
                end -= 1
            return True

        res = []
        # path is a list
        def backtrack(start, path):
            if start >= len(s):
                res.append(path.copy())
            for end in range(start, len(s)):
                substr = s[start:end + 1]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end + 1, path)
                    path.pop()
        backtrack(0, [])
        return res
        