class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        #find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        #reverse the second half of the list
        second = slow.next
        slow.next = None
        prev = None
        
        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        #merge the two halves
        first = head
        second = prev # prev is the head of the reversed second half
        while second:
            temp1 = first.next #save
            temp2 = second.next
            first.next = second #connect
            second.next = temp1           
            #pointers to the next nodes
            first = temp1
            second = temp2