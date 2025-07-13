'''Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.'''




# My logic using condition , same logic as leet code best solution

class Solution:
    def findContentChildren(self, g, s):
        
        g.sort()          
        s.sort()          
        i = 0             
        j = 0            
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:   
                i += 1               
            j += 1
        return i






# Unique Logic

# class Solution:
#     def findContentChildren(self, g, s):
#         max_size = 10001  # assume max size of greed or cookie is 10000

#         # Count frequency of greed factors and cookie sizes
#         greed_count = [0] * max_size
#         cookie_count = [0] * max_size

#         for greed in g:
#             greed_count[greed] += 1

#         for cookie in s:
#             cookie_count[cookie] += 1

#         count = 0
#         # For every greed level from 1 to max_size
#         for i in range(1, max_size):
#             if greed_count[i] == 0:
#                 continue  # no child with this greed level
#             for j in range(i, max_size):  # find any cookie size >= greed level
#                 if cookie_count[j] > 0:
#                     assign = min(greed_count[i], cookie_count[j])
#                     count += assign
#                     greed_count[i] -= assign
#                     cookie_count[j] -= assign
#                     if greed_count[i] == 0:
#                         break  # done with this greed level

#         return count
