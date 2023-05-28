"""
LeetCode link: https://leetcode.com/problems/merge-two-sorted-lists/

Problem description:
--------------------
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

example - 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

example - 2:
    Input: list1 = [], list2 = []
    Output: []

example - 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    dummy = ListNode()      # create a dummy node and point it as head of the sorted list
    tail = dummy            # create another pointer as tail to move this further as we add nodes in sorted order
    while list1 and list2:  # if both lists are non-empty
        if list1.val <= list2.val:  
            tail.next = list1   # if list1's head value is smaller(or equal), point the tail's next to this node. adding nodes to dummy sorted list
            list1 = list1.next  # forward list1 to next node. equivalent to -> take a node from l1 and add to out list
        else: # compliment case
            tail.next = list2
            list2 = list2.next
        tail = tail.next    # once a node is added, advance the tail to point to the new node. 

    if list1: # if anything remains in list1, add it directly to tail since list1 is already sorted
        tail.next = list1
    elif list2: # compliment case
        tail.next = list2

    return dummy.next # we created a dummy node with val=0, and added nodes to the next of this. so return the next node which is the actual start of the sorted list


# test


## helper functions
def create_ll(array):
    head = None
    for idx, value in enumerate(array):
        if idx == 0:
            ll1 = ListNode(val=value)
            head = ll1
        else:
            ll1.next = ListNode(val=value)
            ll1 = ll1.next
    return head


def is_equal_linked_lists(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return not head1 and not head2


def test(l1, l2, out):
    res = mergeTwoLists(create_ll(l1), create_ll(l2))
    return is_equal_linked_lists(create_ll(out), res)


assert test([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
assert test([], [], [])
assert test([], [1], [1])
