'''An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false'''







# Easy ChatGPT code and logic

# class Solution(object):
#     def isRectangleOverlap(self, rec1, rec2):
#         """
#         :type rec1: List[int]
#         :type rec2: List[int]
#         :rtype: bool
#         """
        
#         return not (
#             rec1[2] <= rec2[0] or  
#             rec1[0] >= rec2[2] or  
#             rec1[3] <= rec2[1] or  
#             rec1[1] >= rec2[3]    
#         )








# Mathematical logic 

# def isRectangleOverlap(rec1, rec2):
#     x_overlap = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
#     y_overlap = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
#     return x_overlap > 0 and y_overlap > 0


# def isRectangleOverlap(rec1, rec2):
#     def intervals_overlap(a1, a2, b1, b2):
#         return min(a2, b2) > max(a1, b1)  # strictly greater, not touching

#     x_overlap = intervals_overlap(rec1[0], rec1[2], rec2[0], rec2[2])
#     y_overlap = intervals_overlap(rec1[1], rec1[3], rec2[1], rec2[3])
#     return x_overlap and y_overlap









# Another logic 

# class Solution(object):
#     def isRectangleOverlap(self, rec1, rec2):
#         """
#         :type rec1: List[int]
#         :type rec2: List[int]
#         :rtype: bool
#         """

#         if rec1 == rec2:
#             return True

#         r1x1, r1y1, r1x2, r1y2 = rec1
#         r2x1, r2y1, r2x2, r2y2 = rec2

#         if r1x1 >= r2x2 or r1x2 <= r2x1 or r1y1 >= r2y2 or r1y2 <= r2y1:
#             return False
        
#         return True
        