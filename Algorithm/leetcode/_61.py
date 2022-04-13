# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        if l<2: return head
        temp = head
        ans = None
        count = 0
        if k%l==0: return head
        elif k%l==l-1:
            while temp.next:
                temp = temp.next
            temp.next = head
            ans = head.next
            head.next = None
        else:
            while temp:
                if not temp.next: 
                    temp.next = head
                    break
                elif count==k%l: 
                    ans = temp.next
                    temp2 = temp.next
                    temp.next = None
                    temp = temp2
                else: temp = temp.next
                count += 1
        return ans

