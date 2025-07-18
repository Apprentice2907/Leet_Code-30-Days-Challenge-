'''You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

 

Example 1:


Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
Example 3:

Input: m = 3, n = 3, ops = []
Output: 9'''





# My logic but memory exceeded


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        matrix = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            matrix.append(row)

        for op in ops:
            a, b = op[0], op[1]
            for i in range(a):
                for j in range(b):
                    matrix[i][j] += 1

        max_val = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] > max_val:
                    max_val = matrix[i][j]

        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == max_val:
                    count += 1

        return count
    










# ChatGPT Best solution

# class Solution(object):
#     def maxCount(self, m, n, ops):
#         """
#         :type m: int
#         :type n: int
#         :type ops: List[List[int]]
#         :rtype: int
#         """
#         if not ops:
#             return m * n

#         min_row = m
#         min_col = n

#         for a, b in ops:
#             if a < min_row:
#                 min_row = a
#             if b < min_col:
#                 min_col = b

#         return min_row * min_col