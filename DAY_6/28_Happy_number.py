'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1'''


#  My logic
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
    
        while n != 1 and n not in seen:
            seen.add(n)
            num_str = str(n)
            total = 0
            for i in range(len(num_str)):
                digit = int(num_str[i])
                total += digit * digit
            n = total 
        return n == 1
    



# LeetCode solution best
# class Solution(object):
#     def isHappy(self, n):
#         if(n==1 or n==7):
#             return True
#         elif (n<10):
#             return False
#         else:
#             sum=int()
#             while n>0:
#                 temp=n%10
#                 sum+=temp*temp
#                 n/=10
#             return self.isHappy(sum)
                





# ChatGPT 

# You can use Floyd’s Cycle Detection Algorithm (also called "slow and fast pointer") to detect a loop — without using extra space.
# def get_next(n):
#     total = 0
#     for ch in str(n):
#         digit = int(ch)
#         total += digit * digit
#     return total
# def is_happy(n):
#     slow = n
#     fast = get_next(n)    
#     while fast != 1 and slow != fast:
#         slow = get_next(slow)
#         fast = get_next(get_next(fast))   
#     return fast == 1


# slow moves one step at a time.
# fast moves two steps at a time.
# If there's a loop, slow and fast will meet.
# If we reach 1, it's a happy number.