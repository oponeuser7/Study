class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        for i, val in enumerate(flowerbed):
            if not val:
                
