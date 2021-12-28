# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Title: Middle of the Linked List
    #Approach: iterative approach
    #Explanation: First, you need to iterate through list to get length of the
    #list. Second, iterate through list length//2 times to get the middle of
    #the linked list.
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        for i in range(length//2):
            head = head.next
        return head
