class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        curr = dummy
        carry = 0
        
        # Loop as long as there is a node in l1, l2, or a leftover carry
        while l1 or l2 or carry:
            #default to 0 if we've reached the end of a list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            #total and the new carry
            total = val1 + val2 + carry
            carry = total // 10 #gets the tens digit 
            curr.next = ListNode(total % 10) 

            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next