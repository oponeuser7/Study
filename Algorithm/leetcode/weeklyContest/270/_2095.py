class Solution:
    #One additional approach: slow and fast
    #When you iterate through list to find middle node, there is a trick to
    #make it in O(N/2) time. if you make two pointers named slow and fast and 
    #make fast iterate literally 2 times faster by using it's next.next,
    #you can save time to iterate.
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        temp = head
        while temp.next:
            temp = temp.next
            n += 1
        if n==1: return None
        if n==2:
            head.next = None
            return head
        middle = n//2
        temp = head
        prev = None
        count = 0
        while temp.next:
            if middle==count:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next
            count += 1
        return head
