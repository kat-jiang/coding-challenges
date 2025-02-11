# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def reverseList(head: ListNode) -> ListNode:
        prev = None  # prev pointer, initially pointing to None
        current = head  # current pointer, initially pointing to the head of the list
        
        while current:
            next_node = current.next  # store the next node
            current.next = prev  # reverse the current node's pointer
            prev = current  # move prev to the current node
            current = next_node  # move to the next node
        
        return prev  # prev will be the new head of the reversed list