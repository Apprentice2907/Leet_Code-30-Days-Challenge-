'''
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

 

Example 1:

Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.'''

#  complex but my logic coded using chatGPT

def canWinNim(n):
    memo = {}

    def play(turn, stones):
        if stones == 0:
            return turn != "you"

        key = (turn, stones)
        if key in memo:
            return memo[key]

        if turn == "you":
            memo[key] = any(play("friend", stones - i) for i in [1, 2, 3] if stones >= i)
        else:
            memo[key] = all(play("you", stones - i) for i in [1, 2, 3] if stones >= i)

        return memo[key]

    return play("you", n)








# Simple and best logic

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return n % 4 != 0

