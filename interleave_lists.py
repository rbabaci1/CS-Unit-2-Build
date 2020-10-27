"""
Understand:
Empty list

Odd number list
Input: 1->2->3
Output: 1->3->2

Even number list
Input: 1->2->3->4
Output: 1->3->2->4

Plan:
Use dummy-head to create two lists with even and odd elements
Append even list to end of odd list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        oddDummyHead = ListNode(-1)
        oddCurr = oddDummyHead
        evenDummyHead = ListNode(-1)
        evenCurr = evenDummyHead
        counter = 1
        curr = head
        while curr != None:
            if counter % 2 == 0:
                evenCurr.next = curr
                evenCurr = evenCurr.next
            else:
                oddCurr.next = curr
                oddCurr = oddCurr.next
            counter += 1
            temp = curr.next
            curr.next = None
            curr = temp
        oddCurr.next = evenDummyHead.next
        return oddDummyHead.next
