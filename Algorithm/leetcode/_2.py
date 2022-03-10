# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        ans = temp
        carry = 0
        while l1 or l2 or carry:
            cur = l1.val if l1 else 0+l2.val if l2 else 0+carry
            if cur>9:
                cur = cur-10
                carry = 1
            else: carry = 0
            temp.next = ListNode(cur)
            temp = temp.next
            if l1.next: l1 = l1.next
            if l2.next: l2 = l2.next
        return ans.next

