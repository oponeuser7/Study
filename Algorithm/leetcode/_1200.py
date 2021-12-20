from typing import List

class Solution:
    #Title: Minimum Absolute Difference
    #Approach: Math, sort
    #Explanation: When you sort arr, one of pairs of two adjacence numbers in
    #arr would be the answer because it is sorted. Get minimum absolute Differ
    #ence at first iteration and get pairs which have minimum absolute differe
    #nce at second iteration. So the time complexity would be O(n) and for
    #space it is O(n).
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans, _min = [], float("inf")
        for i in range(len(arr)-1):
            _min = min(_min, abs(arr[i+1]-arr[i]))
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i])==_min:
                ans.append([arr[i], arr[i+1]])
        return ans
