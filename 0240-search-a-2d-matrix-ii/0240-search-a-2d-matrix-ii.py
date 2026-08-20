class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start from top right
        # if val > target: move left -> current column is impossible
        # if val < target: move down -> current row is impossible

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            print(matrix[row][col])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False