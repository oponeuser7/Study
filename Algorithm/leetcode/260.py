class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        appeared = set()
        for num in nums:
            if num not in appeared:
                appeared.add(num)
            else:
                appeared.remove(num)
        return list(appeared)