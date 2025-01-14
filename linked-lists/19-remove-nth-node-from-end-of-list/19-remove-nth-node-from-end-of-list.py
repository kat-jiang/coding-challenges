# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null   n=2
        #   l           r
        # dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null   n=2
        #                    l              r
        #use 2 pointers, l and r, distance between l and r is n + 1
        #when r reaches the end of the linkedlist, l will be at node previous to the node being deleted       

        dummy = ListNode(0, head)
        l = dummy
        r = head
        
        #get r to correct position
        while n > 0 and r:
            r = r.next
            n -= 1
        
        #get r to end of linkedlist
        while r:
            l = l.next
            r = r.next
            
        #delete nth node
        l.next =  l.next.next
        
        return dummy.next