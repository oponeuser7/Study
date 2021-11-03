class Trie:
    def __init__(self):
        self.node = [None for _ in range(26)]
        self.endpoint = False

    def insert(self, word: str) -> None:
        if len(word) < 1:
            self.endpoint = True
            return
        char = ord(word[0])-ord('a')
        if not self.node[char]:
            self.node[char] = Trie()
        self.node[char].insert(word[1:])
    
    def delete(self, word: srr) -> bool:
        if len(word) < 1:
            return False
        char = ord(word[0])-ord('a')
        self.node[char] = self.node[char].delete(word[1:])
        return self.node[char]

    def search(self, word: str) -> bool:
        if len(word) < 1:
            if self.endpoint == True:
                return True
            else:
                return False
        char = ord(word[0])-ord('a')
        if self.node[char]:
            return self.node[char].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) < 1:
            return True
        char = ord(prefix[0])-ord('a')
        if self.node[char]:
            return self.node[char].startsWith(prefix[1:])
        else:
            return False