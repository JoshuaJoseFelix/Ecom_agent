class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
               # 1. Generate the rotated matrix using zip
        rotated = [list(row) for row in zip(*matrix[::-1])]
        
        # 2. Overwrite the original matrix in-place to satisfy the LeetCode constraint
        matrix[:] = rotated