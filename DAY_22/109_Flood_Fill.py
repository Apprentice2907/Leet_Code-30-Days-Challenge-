'''You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:



From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.'''




# Another logic 

# class Solution(object):
#     def floodFill(self, image, sr, sc, color):
#         """
#         :type image: List[List[int]]
#         :type sr: int
#         :type sc: int
#         :type color: int
#         :rtype: List[List[int]]
#         """
#         stack = [(sr, sc)]
#         m = len(image)
#         n = len(image[0])
#         o_c = image[sr][sc]
#         if o_c == color:
#             return image
#         while stack:
#             o_p = stack.pop()
#             curr_r = o_p[0]
#             curr_c = o_p[1]
#             if image[curr_r][curr_c] == o_c:
#                 image[curr_r][curr_c] = color
#                 for change_i in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#                     new_r = curr_r + change_i[0]
#                     new_c = curr_c + change_i[1]
#                     if 0 <= new_r < m and 0 <= new_c < n:
#                         if image[new_r][new_c] == o_c:
#                             stack.append((new_r, new_c))
#         return image


        








# Best logic 

# class Solution(object):
#     def floodFill(self, image, sr, sc, color):
#         """
#         :type image: List[List[int]]
#         :type sr: int
#         :type sc: int
#         :type color: int
#         :rtype: List[List[int]]
#         """
#         original_color = image[sr][sc]
#         if original_color == color:
#             return image

#         rows, cols = len(image), len(image[0])

#         def dfs(r, c):
#             if r < 0 or r >= rows or c < 0 or c >= cols:
#                 return
#             if image[r][c] != original_color:
#                 return

#             image[r][c] = color
#             dfs(r + 1, c)
#             dfs(r - 1, c)
#             dfs(r, c + 1)
#             dfs(r, c - 1)

#         dfs(sr, sc)
#         return image
