class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                if i==j or digits[i]==0: continue
                for k in range(n):
                    if k==i or k==j: continue
                    if digits[k]%2==0:
                        ans.add(digits[i]*100+digits[j]*10+digits[k])
        return sorted(list(ans))
