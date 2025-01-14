# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        one = []
        two = []
        
        while l1:
            one.append(l1.val)
            l1 =  l1.next
        while l2:
            two.append(l2.val)
            l2 = l2.next
            
        one = int("".join(map(str, one[::-1])))
        two = int("".join(map(str, two[::-1])))
        
        sum = one + two
        
        for num in str(sum)[::-1]:
            curr.next = ListNode(num)
            curr = curr.next
            
        return dummy.next
        