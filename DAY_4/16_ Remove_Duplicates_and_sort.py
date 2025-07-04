'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]'''





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head






'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        # Step 1: Convert linked list to list of values
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        # Step 2: Remove duplicates using set, then sort
        unique_sorted_values = sorted(set(values))

        # Step 3: Convert list back to linked list
        dummy = ListNode(0)
        current = dummy
        for val in unique_sorted_values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
'''