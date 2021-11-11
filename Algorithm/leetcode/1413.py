class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _min, _sum = 0, 0
        for num in nums:
            _sum += num
            _min = min(_sum, _min)
        return 1 - _min