
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        prev = 0


        
        while l1 or l2 or prev > 0:

            if l1 and l2:
                curr.next = ListNode()
                curr = curr.next
                curr.val = (l1.val + l2.val + prev) % 10
                prev = (l1.val + l2.val + prev) // 10
                l1 = l1.next
                l2 = l2 . next
                
            elif l1:

                curr.next = ListNode()
                curr = curr.next
                curr.val = (l1.val + prev) % 10
                prev = (l1.val + prev) // 10
                l1 = l1.next
            
            elif l2:
                curr.next = ListNode()
                curr = curr.next
                curr.val = (l2.val + prev) % 10
                prev = (l2.val + prev) // 10
                l2 = l2.next
            
            else:
                curr.next = ListNode()
                curr = curr.next
                curr.val = prev
                prev = 0
            

        return dummy.next









                