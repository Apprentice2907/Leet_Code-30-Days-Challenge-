'''At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 

Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.'''








# My logic using loop and conditional 

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        earning = []
        for bill in bills:
            if bill == 5:
                earning.append(5)
            elif bill == 10:
                if 5 in earning:
                    earning.remove(5)
                    earning.append(10)
                else:
                    return False
            elif bill == 20:
                if 10 in earning and 5 in earning:
                    earning.remove(10)
                    earning.remove(5)
                    earning.append(20)
                elif earning.count(5) >= 3:
                    earning.remove(5)
                    earning.remove(5)
                    earning.remove(5)
                    earning.append(20)
                else:
                    return False
        return True




# Leet code best solution

# class Solution(object):
#     def lemonadeChange(self, bills):
#         five = 0  # number of $5 bills we have
#         ten = 0   # number of $10 bills we have

#         for bill in bills:
#             if bill == 5:
#                 five += 1  # no change needed
#             elif bill == 10:
#                 if five == 0:
#                     return False  # can't give $5 change
#                 five -= 1
#                 ten += 1
#             elif bill == 20:
#                 # Prefer to give $10 + $5 as change
#                 if ten > 0 and five > 0:
#                     ten -= 1
#                     five -= 1
#                 elif five >= 3:
#                     five -= 3
#                 else:
#                     return False  # can't give $15 change
#         return True