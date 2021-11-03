# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        points = []
        temp = head.next
        prev = head
        index = 1
        while True:
            if temp.next is not None:
                nxt = temp.next
                if (prev.val < temp.val > nxt.val) or (prev.val > temp.val < nxt.val):
                    points.append(index)
                prev = temp
                temp = nxt
                index += 1
            else:
                if len(points)<2:
                    return [-1,-1]
                else:
                    max_d = points[len(points)-1] - points[0]
                    min_d = 100000
                    for i in range(len(points)-1):
                        min_d = min(points[i+1]-points[i], min_d)
                    return [min_d, max_d]