# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = head.next
        dummy = ListNode(next=head)

        curr = head
        while dummy.next and dummy.next.next:
            dummy.next = curr.next
            curr.next = curr.next.next
            dummy.next.next = curr

            dummy = curr
            curr = curr.next
        

        return newHead

        