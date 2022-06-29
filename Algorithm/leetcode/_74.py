from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix)**2
        l, r, mid = 0, length, 0
        while left<right:
            mid = (l+r)//2
            if matrix[mid] <= target:
                l = mid-1
            else:
                r = mid+1
        return mid==target


