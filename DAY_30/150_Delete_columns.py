'''You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

 

Example 1:

Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
Example 2:

Input: strs = ["a","b"]
Output: 0
Explanation: The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.
Example 3:

Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.'''










# My logic using simple logic  

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        n = len(strs)
        m = len(strs[0])

        for col in range(m):
            for row in range(n - 1):
                if strs[row][col] > strs[row + 1][col]:
                    count += 1
                    break
        return count
        








    


# Leet code best solution

# class Solution(object):
#     def minDeletionSize(self, strs):
        
#         count = 0
#         for col in range(len(strs[0])):
#             for row in range(1, len(strs)):
#                 if strs[row][col] < strs[row-1][col]:
#                     count += 1
#                     break
#         return count