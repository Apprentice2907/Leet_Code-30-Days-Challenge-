'''An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).z
Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.


Example 1:


Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Example 2:


Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138'''








# Simple and mathematical logic

class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        result = []

        for i in range(m):
            row = []
            for j in range(n):
                total = 0
                count = 0

                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1

                row.append(total // count)
            result.append(row)

        return result






# Another logic

# class Solution(object):
#     def imageSmoother(self, img):
#         dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
#         newimg = [[0]*len(img[0]) for _ in range(len(img))]
#         for i in range(len(img)):
#             for j in range(len(img[i])):
#                 total, cnt = 0, 0
#                 for r, c in dirs:
#                     nr, nc = i + r, j + c
#                     if 0 <= nr < len(img) and 0 <= nc < len(img[i]):
#                         total += img[nr][nc]
#                         cnt += 1
#                 newimg[i][j] = total//cnt
                
#         return newimg
        