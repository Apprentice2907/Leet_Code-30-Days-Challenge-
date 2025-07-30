'''You are given an integer array deck where deck[i] represents the number written on the ith card.

Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.

 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.'''











# My logic 
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        uniq = set(deck)
        freq = []

        for val in uniq:
            count = 0
            for card in deck:
                if card == val:
                    count += 1
            freq.append(count)

        minf = min(freq)

        for size in range(2, minf + 1):
            valid = True
            for f in freq:
                if f % size != 0:
                    valid = False
                    break
            if valid:
                return True

        return False















# Leet code best solution and ChatGPT suggested using GCD logic

# class Solution(object):
#     def hasGroupsSizeX(self, deck):
#         count= Counter(deck).values()
#         def greatestCommonDivisor(a, b):
#             while b:
#                 a, b = b, a % b
#             return a    
#         def gcd_list(numbers):
#             result = numbers[0]
#             for num in numbers[1:]:
#                 result = greatestCommonDivisor(result, num)
#             return result
#         if gcd_list(count) >1:
#             return True
#         else:
#             return False

