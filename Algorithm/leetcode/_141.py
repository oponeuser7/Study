# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #Title: Linked List Cycle
    #Approach: Iterative way
    #Explanation: When 10^4 is maximam number of the nodes in the list you can
    #say that there is a cycle in the list if you did not meet the tail of the
    #list after iterating through list 10^4 times.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        for i in range(10000):
            if not head.next: return False
            head = head.next
        return True           
