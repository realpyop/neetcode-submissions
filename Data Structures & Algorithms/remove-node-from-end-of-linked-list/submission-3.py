# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # Two pointer approrach (with right pointer shifted nth time then move till end of list)
        left, right = dummy, head
        for i in range(n-1):
            right = right.next
        
        while right and right.next:
            right = right.next
            left = left.next
        
        # Left should be prev value before nth from back of list
        left.next = left.next.next

        return dummy.next
        