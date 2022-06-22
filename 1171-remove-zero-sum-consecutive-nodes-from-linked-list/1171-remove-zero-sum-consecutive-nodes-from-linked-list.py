# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node and point to head of the list
        # Need 2 pointers to track sum to 0
        # Iterate over the node
        # Store the current sum
        # Add the value of the node to the current sum
        #   If the consecutive sum is 0, delete nodes that sum up to 0
        #   Otherwise, move to next node
        # Then move the pointer at head to next node
        # Return the head which is pointer.next
        
        pointer = ListNode(float("inf"))
        pointer.next = head
        
        curr = head
        head = pointer

        while head:
            current_sum = 0

            while curr:
                current_sum += curr.val

                if current_sum == 0:
                    head.next = curr.next

                curr = curr.next

            head = head.next

            if head:
                curr = head.next

        return pointer.next  