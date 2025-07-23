'''Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 '''








# My logic using matrix

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for row in range(m):
            val = matrix[row][0]
            i, j = row, 0
            while i + 1 < m and j + 1 < n:
                i += 1
                j += 1
                if matrix[i][j] != val:
                    return False

        for col in range(1, n):
            val = matrix[0][col]
            i, j = 0, col
            while i + 1 < m and j + 1 < n:
                i += 1
                j += 1
                if matrix[i][j] != val:
                    return False

        return True











# Best Logic ChatGPT

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
