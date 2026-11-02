# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node because we are returning a linkedlist
        dummy = ListNode()
        curr = dummy

        # 1: Loop through while l1 or l2 are not None
        carry = 0
        while l1 or l2 or carry:
        # 2: Create v1 and v2 variable if the node has a val else 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

        # 3: Calculate carry over and only get the last digit of the sum
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

        # 4: Update pointer
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            
        # 5: EDGE CASE -> Loop while carry still not 0 because case like 7 + 8 = 15

        return dummy.next
