# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #In this solution I did not use prev pointer. Prev pointer may need a dummy node which becomes
        #a prev pointer of the FIRST node. In first while roof, starting from head, you check if current
        #node is not null and current node value is equal to target value. if it is, move head pointer to
        #the next node, which means you happens to delete current node from list. In second while roof,
        #you check if there is a next node of current node and it's value is equal to the target value.
        #If condition is right, you set current node's next node to it's next-next node, which means deleting
        #next node of current node from list. From the end of first while roof, you don't need to check the
        #value of current node because at the time first while roof endend, the node head pointer is pointing
        #MUST have different value from target value. This solve's time complexity would be O(n) since it's 
        #iterating through every nodes once and space complexity would be O(1) since I don't know, it's
        #iterative and no data structure is used so O(1) won't be a hard guess.
        while head and head.val==val:
            head = head.next
        temp = head
        while temp:
            if temp.next and temp.next.val==val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head