'''You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.

 

Example 1:


Input: grid = [[1,2],[3,4]]
Output: 34
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 3:


Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 '''









# My logic but chatGPT coded

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
     
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h > 0:
                    area += 6 * h
                    area -= 2 * (h - 1)

                if i + 1 < n:
                    area -= 2 * min(grid[i][j], grid[i+1][j])

                if j + 1 < n:
                    area -= 2 * min(grid[i][j], grid[i][j+1])

        return area













# Leet Code best solution and easy to understand

# class Solution(object):
#     def surfaceArea(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         total = 2 * len(grid) * len(grid[0])
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 height = grid[i][j]
#                 if height == 0:
#                     total -= 2
#                     continue
#                 if i+1 == len(grid):
#                     total += height
#                 elif height > grid[i+1][j]:
#                     total += height - grid[i+1][j]
#                 if j+1 == len(grid[0]):
#                     total += height
#                 elif height > grid[i][j+1]:
#                     total += height - grid[i][j+1]
#                 if i == 0:
#                     total += height
#                 elif height > grid[i-1][j]:
#                     total += height - grid[i-1][j]
#                 if j == 0:
#                     total += height
#                 elif height > grid[i][j-1]:
#                     total += height - grid[i][j-1]
#         return total
                
                