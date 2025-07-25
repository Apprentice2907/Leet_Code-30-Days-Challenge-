'''You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].'''










# My logic, chatGPT coded

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        score_with_index = []
        for i in range(n):
            score_with_index.append((score[i], i))
        score_with_index.sort(reverse=True)
        result = ["" for _ in range(n)]

        for rank, (value, index) in enumerate(score_with_index):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)

        return result
    










# leetcode Best

# class Solution(object):
#     def findRelativeRanks(self, score):
#         ss=sorted(score, reverse=True)
#         ranks = {ss[i]: str(i + 1) for i in range(len(score))}
#         ranks[ss[0]] = "Gold Medal"
#         if len(score) > 1:
#             ranks[ss[1]] = "Silver Medal"
#         if len(score) > 2:
#             ranks[ss[2]] = "Bronze Medal"
#         return [ranks[s] for s in score]       