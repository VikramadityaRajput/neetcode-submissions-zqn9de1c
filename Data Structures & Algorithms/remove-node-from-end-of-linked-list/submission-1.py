# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        traversal = length - n
        curr = head
        num = 0
        if traversal == 0:
            return head.next
        while curr:
            if num == traversal - 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
            num += 1
        return head

