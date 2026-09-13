# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None
        
        prev = None

        while secondHalf:
            tmp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = tmp

        firstHalf = head
        secondHalf= prev


        while firstHalf.next:
            tmp = firstHalf.next
            firstHalf.next = secondHalf
            tmp2 = secondHalf.next
            secondHalf.next = tmp
            firstHalf = tmp
            secondHalf = tmp2
           
        
        firstHalf.next = secondHalf

        
        return 
        
        
                
            











        