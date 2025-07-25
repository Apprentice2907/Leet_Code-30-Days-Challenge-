'''Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]'''







# My logic using reverse and conditions best logic

class Solution:
    def flipAndInvertImage(self, image):
        result = []

        for row in image:
            revrow = row[::-1]
            newrow = []

            for val in revrow:
                if val == 1:
                    newrow.append(0)
                else:
                    newrow.append(1)

            result.append(newrow)

        return result








# Least efficient code

# class Solution(object):
#     def flipAndInvertImage(self, image):
#         for row in image:
#             n = len(row)
#             for i in range((n + 1) // 2):
#                 row[i], row[n - 1 - i] = row[n - 1 - i] ^ 1, row[i] ^ 1
#         return image