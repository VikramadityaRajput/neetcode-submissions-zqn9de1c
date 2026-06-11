"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        curr = head #create a copy of every node
        otn = {}
        while curr:
            otn[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head #assign the pointers
        while curr:
            if curr.next: #next
                otn[curr].next = otn[curr.next]
            if curr.random: #random
                otn[curr].random = otn[curr.random]
            curr = curr.next
        return otn[head]