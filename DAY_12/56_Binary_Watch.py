'''A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []'''









# ChatGPT logic 

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        if turnedOn < 0 or turnedOn > 10:          
            return []

        res = []
        for h in range(12):                        
            for m in range(60):                   
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    res.append("%d:%02d" % (h, m)) 
        return res







# Simple and easy understanding logic

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        result = []

        for hour in range(12):
            for minute in range(60):
                hour_leds = bin(hour).count('1')
                minute_leds = bin(minute).count('1')
                if hour_leds + minute_leds == turnedOn:
                    result.append(f"{hour}:{minute:02d}")

        return result







# Leetcode solution

# class Solution(object):
#     def readBinaryWatch(self, turnedOn):
#         """
#         :type turnedOn: int
#         :rtype: List[str]
#         """
#         result = []
#         for hour in range(12):
#             for minute in range(60):
#                 if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
#                     result.append("{}:{:02d}".format(hour, minute))
#         return result









# My logic

# class Solution(object):
#     def readBinaryWatch(self, turnedOn):
#         """
#         :type turnedOn: int
#         :rtype: List[str]
#         """
#         ans=[]
#         for h in range(12):
#             for m in range(60):
#                 h_bits = bin(h).count("1")
#                 m_bits = bin(m).count("1")

#                 if h_bits + m_bits == turnedOn:
#                     new_ans= str(h) + ":"
#                     if m<10:
#                         new_ans = new_ans + "0" + str(m)
#                     else:
#                         new_ans = new_ans + str(m)

#                     ans.append(new_ans)
#         return ans