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

# the above is O(n^2) solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head: ListNode) -> ListNode:
    # Create a dummy node that helps handle edge cases like removing the head
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = {0: dummy}  # This will store the first occurrence of each prefix sum
    
    # Traverse through the linked list
    current = head
    total_sum = 0
    
    while current:
        total_sum += current.val  # Add the current node's value to the total_sum
        
        if total_sum in prefix_sum:  # Check if this prefix sum has been encountered before
            prev = prefix_sum[total_sum]  # Get the node that corresponds to the previous occurrence of this sum
            # Remove all nodes between prev and current by setting prev's next pointer to current.next
            node = prev.next  # Start iterating from the node after prev (the first node to be considered)
            temp_sum = total_sum  # Start the running sum with total_sum (probably the sum up to the prev node)

            while node != current:  # Iterate through nodes until we reach the current node
                temp_sum += node.val  # Add the value of each node to temp_sum
                node = node.next  # Move to the next node in the list
                del prefix_sum[temp_sum]  # Remove the sums that were part of the zero-sum sequence
            
            prev.next = current.next  # Remove the zero-sum subsequence
        else:
            prefix_sum[total_sum] = current  # Store the current node as part of the prefix sum
        
        current = current.next  # Move to the next node
    
    return dummy.next  # Return the modified list starting from the node after dummy
