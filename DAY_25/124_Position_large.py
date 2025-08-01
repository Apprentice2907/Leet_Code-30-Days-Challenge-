'''In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

 

Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.
Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".'''











# My logic and little bit chatGPT coded

class Solution:
    def largeGroupPositions(self, s):
        result = []
        count = 1
        start = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                if count >= 3:
                    result.append([start, i - 1])
                count = 1
                start = i

        if count >= 3:
            result.append([start, len(s) - 1])

        return result










# Leet code best solution

# class Solution(object):
#     def largeGroupPositions(self, s):
        
#         res=[]
#         n=len(s)
#         i=0

#         while i<n:
#             j=i
#             while j<n and s[j]==s[i]:
#                 j+=1

#             if j-i>=3:
#                 res.append([i,j-1])
#             i=j

#         return res            
        













# Another logic but different

# class Solution(object):
#     def largeGroupPositions(self, s):
#         res, n, i = [], len(s), 0
#         while i < n:
#             j = i
#             while j < n and s[j] == s[i]:
#                 j += 1
#             if j - i >= 3:
#                 res.append([i, j-1])
#             i = j
#         return res
        