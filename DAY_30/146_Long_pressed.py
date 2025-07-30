'''Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.'''





# My logic and best leet code solution

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name)








# Another logic 


# class Solution(object):
#     def isLongPressedName(self, name, typed):
#         group_1 = [[name[0],1]]
#         for i in range(1,len(name)):
#             if name[i] == name[i-1]:
#                 group_1[-1][-1] += 1
#             else:
#                 group_1.append([name[i],1])
#         group_2 = [[typed[0],1]]
#         for i in range(1,len(typed)):
#             if typed[i] == typed[i-1]:
#                 group_2[-1][-1]+=1
#             else:
#                 group_2.append([typed[i],1])
        
#         if len(group_1) != len(group_2):
#             return False
#         else:
#             for i in range(len(group_2)):
#                 if (group_2[i][-1] < group_1[i][-1]) or (group_2[i][0]!=group_1[i][0]):
#                     return False
#         return True
        





        