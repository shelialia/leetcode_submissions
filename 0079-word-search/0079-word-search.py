class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS to find all letters in the word
        # Each time:
        # 1. Check if word has been found
        # 2. in bounds check
        # 3. Mark the char as being used first (so that it is not reused in the same path again)
        # 3. Dfs on neighbours to search for remaining parts of word
        # 4. Unmark the char
        def backtrack(row, col, index) -> bool:
            # dfs base case, the entire word has been found
            # hence arrive in the next loop. should terminate. 
            if index == len(word):
                return True

            # Out of bounds case
            # Wrong character case
            if (row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1) or board[row][col] != word[index]:
                return False

            # Mark the entry in board so that same path does not re-use it
            # After dfs, we can un-mark the entry
            temp = board[row][col]
            board[row][col] = "."
            is_found = (
                backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1)
            )
            board[row][col] = temp

            # DFS returns whether the word is found
            return is_found

        # Carry out dfs on every entry on board because we do not know where the word starts at
        for row in range(len(board)):
            for col in range((len(board[0]))):
                if backtrack(row, col, 0):
                    return True
        return False