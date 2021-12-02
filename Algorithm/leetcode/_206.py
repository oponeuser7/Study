# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Explanation
        #step1: save current next node
        #step2: make current node point prev node
        #step3: move on to next node using saved next node
        #step4: so on
        #tip: you need initial dummy node for prev node at head
        temp1, temp2 = None, None
        cur = head
        while cur:
            temp2 = cur.next
            cur.next = temp1
            temp1 = cur
            cur = temp2
        return head
