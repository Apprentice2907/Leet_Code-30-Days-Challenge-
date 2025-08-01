'''You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.
 

Example 1:

Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explanation: You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.
Example 2:

Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
Output: [2,4]
Explanation: You can write s as follows:
bbbcccdddaa  // 98 pixels wide
a            // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.'''











# My logic using mapping 

class Solution(object):
    def numberOfLines(self, widths, s):
        letters = "abcdefghijklmnopqrstuvwxyz"
        mapping = {}
        for i in range(len(letters)):
            mapping[letters[i]] = widths[i]

        lines = 1
        width = 0

        for ch in s:
            w = mapping[ch]
            if width + w > 100:
                lines += 1
                width = w
            else:
                width += w

        return [lines, width]




# Leet code Best solution

# class Solution(object):
#     def numberOfLines(self, widths, s):
#         """
#         :type widths: List[int]
#         :type s: str
#         :rtype: List[int]
#         """
        
#         max_width = 100
#         lines = 1
#         current_width = 0

#         for char in s:
#             w = widths[ord(char) - ord('a')]
#             if current_width + w > max_width:
#                 lines += 1
#                 current_width = w
#             else:
#                 current_width += w

#         return [lines, current_width]




