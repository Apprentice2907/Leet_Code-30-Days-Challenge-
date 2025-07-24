'''You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0'''



# MY logic but chatGPT coded
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_subs = [jewels[i:j] for i in range(len(jewels)) for j in range(i+1, len(jewels)+1)]
        stone_subs = [stones[i:j] for i in range(len(stones)) for j in range(i+1, len(stones)+1)]

        count = 0
        for sub in jewel_subs:
            if len(sub) == 1:
                count += stone_subs.count(sub)
        return count



# Simple and loigcal code

# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         count = 0
#         for j in jewels:
#             count += stones.count(j)
#         return count


# Best leet code solution
# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         ans=0
#         for i in stones:
#             if i in jewels:
#                 ans+=1
#         return ans
        