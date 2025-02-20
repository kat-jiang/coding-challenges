"""
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle of list
        #   using slow and fast pointer, fast pointer moves at 2x speed
        #   when fast pointer reaches the end, slow will be in the middle
        #reverse 2nd half of list
        #   prev, curr, next
        #   save next node
        #   point curr.next to prev
        #   point prev to curr
        #   point curr to next
        #merge the 2 lists
        #   store l1 and l2 next
        #   set l1 next to l2
        #   set l2 next to l1.next
        #   point to l1 and l2 next
        slow = head
        fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None # split the list in half
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        l1 = head
        l2 = prev

        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2
