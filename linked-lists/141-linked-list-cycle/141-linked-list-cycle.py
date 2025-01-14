# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        current = head

        while current:
            if current not in seen:
                seen.add(current)
                current = current.next
            else:
                return True

        return False
