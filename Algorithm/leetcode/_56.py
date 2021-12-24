class Solution:
    #Title: Merge Intervals
    #Approach: sort and iteration
    #Explanation: When you sort input list, problem becomes simpler. If prev end
    #is bigger than current start, intervals should be merged. If not, create
    #interval using start and prev value and append it to ans list. There is a
    #corner case where prev end is bigger than current end. Considering these
    #cases, we must pick max(prev_end, cur_end) for prev value when merging the
    #intervals.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        start, end = intervals[0][0], intervals[0][0]
        for i in intervals:
            if end<i[0]:
                ans.append([start,end])
                start, end = i[0], i[1]
            else:
                end = max(end, i[1])
        ans.append([start,end])
        return ans

