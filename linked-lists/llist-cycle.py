import unittest
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: List[ListNode]) -> bool:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    """
    seen = set()

    current = head

    while current:
        if current not in seen:
            seen.add(current)
            current = current.next
        else:
            return True

    return False

#Runtime complexity: O(n)
#Spacetime complexity: O(n)

class TestHandler(unittest.TestCase):
    def test_cycle(self):
        """
        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
        """
        node3 = ListNode(3)
        node2 = ListNode(2)
        node0 = ListNode(0)
        node4 = ListNode(-4)
        node3.next = node2
        node2.next = node0
        node0.next = node4
        node4.next = node2

        self.assertTrue(has_cycle(node3))

    def test_no_cycle(self):
        """
        Input: head = [1,2], pos = -1
        Output: false
        Explanation: There is no cycle in the linked list.
        """
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2

        self.assertFalse(has_cycle(node1))


testclass = unittest.main(exit=False)
if testclass.result.wasSuccessful():
    print("Test pass -- woohoo!")
