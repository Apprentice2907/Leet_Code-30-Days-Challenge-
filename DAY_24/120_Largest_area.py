'''Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000'''








# Simple and mathematical logic 

class Solution(object):
    def largestTriangleArea(self, points):
        def area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0

        max_area = 0
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a = area(points[i], points[j], points[k])
                    if a > max_area:
                        max_area = a

        return max_area














# Leet code best solution

# class Solution:
#     def largestTriangleArea(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: float
#         """
#         n = len(points)
#         max_area = 0
        
#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):
#                     x1, y1 = points[i]
#                     x2, y2 = points[j]
#                     x3, y3 = points[k]
                    
#                     # Calculate area using the Shoelace formula
#                     area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
#                     max_area = max(max_area, area)
        
#         return max_area