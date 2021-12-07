# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #title: Convert Binary Number in a Linked List to Interger
    #explanation: You can you a single integer variable for ans memory.
    #When moving to next node, it is same as right-shifting sum till now
    #and adding next node value.
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans*2 + head.val
            head = head.next
        return ans
