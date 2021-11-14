class CombinationIterator:
    powerset = []
    index = 0
    def __init__(self, string: str, length: int):
        self.index = -1
        self.powerset = list(combinations(string, length))

    def next(self) -> str:
        self.index += 1
        return "".join(self.powerset[self.index])

    def hasNext(self) -> bool:
        return len(self.powerset) > self.index+1


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()