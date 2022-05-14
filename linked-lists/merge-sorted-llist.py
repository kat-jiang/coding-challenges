import unittest
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_llist(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    """
    #make merged linked list to return
    #merged list will contain the list of merged nodes starting with current_node
    #current_node will point to the last node of the merged linked list as it builds
    merged_llist = current_node = ListNode()

    #compare nodes in list1 and list2 - loop breaks when either list is empty
    #Pointer starts at head node of each list
    #compare the nodes: lower value is added as next node in merged linked list
    #update pointer in that list to it's next node
    #update current node pointer to the newly added node in merged list
    while list1 and list2:
        if list1.val < list2.val:
            current_node.next = list1
            list1, current_node = list1.next, list1
        else:
            current_node.next = list2
            list2, current_node = list2.next, list2

    #check to see which list still has nodes remaining
    #add that list's node as the next node in merged list
    if list1 or list2:
        current_node.next = list1 if list1 else list2

    return merged_llist.next

#Runtime complexity: O(n)
#Spacetime complexity: O(n)

class TestHandler(unittest.TestCase):

    def test_merge_list(self):
        """
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        """
        node1 = ListNode(1)
        node2 = ListNode(2)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node4

        node2_1 = ListNode(1)
        node2_3 = ListNode(3)
        node2_4 = ListNode(4)
        node2_1.next = node2_3
        node2_3.next = node2_4

        result = merge_two_llist(node1, node2_1)
        self.assertEqual(result.val, 1)
        
        values = []
        while result:
            values.append(result.val)
            result = result.next
        self.assertEqual(values, [1,1,2,3,4,4])



testclass = unittest.main(exit=False)
if testclass.result.wasSuccessful():
    print("Test pass -- woohoo!")
