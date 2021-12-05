class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class StreamChecker:
    #Title: Stream of Characters
    #Appoach: Trie
    #Why?: It is obvious that this is a trie problem. Yet there are two complex
    #points. First it is not prefix but suffix. You can solve this problem by
    #just inserting a word into a trie by reversed order. Second the input is
    #a buffer. You just need to keep appending character to the buffer and 
    #finding match suffix. In trie, you need to properties for node. 
    def __init__(self, words: List[str]):
        self.stream = ""
        self.root = TrieNode()
        for word in words:
            temp = self.root
            for i in range(len(word)-1, -1, -1):
                char = word[i]
                if char not in temp.children: temp.children[char] = TrieNode()
                temp = temp.children[char]
            temp.end = True

    def query(self, letter: str) -> bool:
        self.stream += letter
        temp = self.root
        for i in range(len(self.stream)-1, -1, -1):
            if temp.end: return True
            char = self.stream[i]
            if char in temp.children: temp = temp.children[char]
            else: return False
        return temp.end
