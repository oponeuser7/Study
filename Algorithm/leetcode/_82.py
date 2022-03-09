# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Title:Remove Duplicates from Sorted List II
    #Explanation: First you need to check duplicates by iterating through list.
    #And remove duplicated nodes iterating through list once again. You just
    #need to use 'remove from list' technic to remove node: link prev node to
    #next node.
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen, dup = set(), set()
        temp = head
        while temp:
            cur = temp.val
            if cur in seen: dup.add(cur)
            else: seen.add(cur)
            temp = temp.next
        dummy = ListNode(101)
        dummy.next = head
        temp = head
        prev, nxt = dummy, None
        while temp:
            cur = temp.val
            nxt = temp.next
            if cur in dup:
                if temp is head: head = nxt
                else: prev.next = nxt if nxt else None
            else: prev = temp
            temp = temp.next
        return head           
