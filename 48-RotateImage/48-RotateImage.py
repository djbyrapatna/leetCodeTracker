# Last updated: 8/18/2025, 6:26:24 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        # first transpose the the values the bottom half
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # then swap all the rows
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        