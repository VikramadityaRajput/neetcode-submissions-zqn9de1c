# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#if theres a cycle then a loop would go forever. if we have done more loops then
        curr = head
        ahead = head
        while curr and ahead:
            curr = curr.next
            if ahead.next == None:
                return False
            ahead = ahead.next.next
            if curr == ahead:
                return True
        return False