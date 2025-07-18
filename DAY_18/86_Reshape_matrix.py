'''In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
'''







# My logic simple and easy 
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        ele = []
        for i in range(m):
            for j in range(n):
                ele.append(mat[i][j])

        if len(ele) < r * c or len(ele) > r * c:
            return mat

        nmat = []
        index = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(ele[index])
                index += 1
            nmat.append(row)

        return nmat

            









# Leet Code Best Solution 


# class Solution(object):
#     def matrixReshape(self, mat, r, c):
#         """
#         :type mat: List[List[int]]
#         :type r: int
#         :type c: int
#         :rtype: List[List[int]]
#         """
#         m, n = len(mat), len(mat[0])
#         if (m * n) != (r * c):
#             return mat

#         n_strt_idx = 0
#         n_up_lim = c
#         m_idx = 0
#         reshaped_mat = []
#         reshaped_mat_row = []
#         while m_idx < m:
#             reshaped_mat_row.extend(mat[m_idx][n_strt_idx : n_up_lim])                
#             if len(reshaped_mat_row) == c:
#                 reshaped_mat.append(reshaped_mat_row)
#                 reshaped_mat_row = []

#             if n_up_lim > n:
#                 n_strt_idx = 0
#                 n_up_lim = c - len(reshaped_mat_row)
#                 m_idx += 1
#             else:
#                 n_strt_idx = n_up_lim
#                 n_up_lim += c

#         return reshaped_mat
                

            

                

        
        