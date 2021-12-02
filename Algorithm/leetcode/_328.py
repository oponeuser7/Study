#class ListNode:
# def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
    #Title: Odd Even Linked List
    #Solution: iterative
    #In list problems, it's good to draw nodes and links at a real paper.
    #First, you have to get tail of the linked list. The list's length n could
    #be 0 which also means head could be None so check if it is at the start
    #of coding. When you get the tail, start iterating. From the fact that
    #you are starting from odd node because it's the first node, you just need
    #to do same actions at each node. Pop next node and attach it to the tail.
    #But where to stop iterating is kind of vague. And you cand find that
    #you do this node-switching thing exactly N(length of list)//2 times.
    #So you have to iterate through list N//2 times.

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur ,end = head, None
        while cur.next: cur = cur.next
        end = cur
        tail = end
        cur = head
        while cur is not end and cur.next is not end:
            tail.next = cur.next
            cur.next = cur.next.next
            tail = tail.next
            tail.next = None
            cur = cur.next
        return head

