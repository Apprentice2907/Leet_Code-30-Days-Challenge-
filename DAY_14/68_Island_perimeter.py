'''You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4'''








# My logic using hints and discussions in leetcoe and coded by chatGPT

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Top
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    # Bottom
                    if i == rows-1 or grid[i+1][j] == 0:
                        perimeter += 1
                    # Left
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    # Right
                    if j == cols-1 or grid[i][j+1] == 0:
                        perimeter += 1
        return perimeter





# Leet code best 
# class Solution(object):
#     def islandPerimeter(self, grid):
#         r, c, s = len(grid), len(grid[0]), 0
#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j]:
#                     s += 4
#                     if i and grid[i-1][j]:
#                         s -= 2
#                     if j and grid[i][j-1]:
#                         s -= 2
#         return s