'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()   
        tail = dummy         

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next


# Best Output ChatGPT
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         dummy = ListNode()
#         current = dummy

#         while list1 and list2:
#             if list1.val <= list2.val:
#                 current.next, list1 = list1, list1.next
#             else:
#                 current.next, list2 = list2, list2.next
#             current = current.next

#         current.next = list1 or list2
#         return dummy.next



# Best Output LeetCode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         dummy = ListNode()
#         l = dummy
#         it1 = list1
#         it2 = list2

#         while it1 != None and it2 != None:
#             if it1.val < it2.val:
#                  l.next = ListNode(it1.val)
#                  it1 = it1.next
#             else:
#                 l.next = ListNode(it2.val)
#                 it2 = it2.next
#             l = l.next

#         if it1 != None:
#             l.next = it1
            
#         if it2 != None:
#             l.next = it2

#         return dummy.next