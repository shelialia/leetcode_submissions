class Solution:
    def isValid(self, s: str) -> bool:
        # First In Last Out (FILO) - Stack
        # Can enforce parenthesis matching
        close_to_open_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        open_set = {"(", "{", "["}
        stack = []
        for char in s:
            if char in open_set:
                stack.append(char)
            # char is a closing bracket
            elif not stack or close_to_open_map[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack