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

    def flip(self,head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        head = self.flip(head)
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        for i in range(n-1):
            curr = curr.next

        curr.next = curr.next.next

        head = self.flip(dummy.next)

        return head


            






