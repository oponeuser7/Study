import copy

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

def findWords(board, words):
    width = len(board[0])
    height = len(board)
    dx = (1,-1,0,0)
    dy = (0,0,1,-1)
    trie = Trie()
    result_set = set()
    left_set = set()
    for i in words:
        left_set.add(i)
    for i in words:
        trie.insert(i)
    for i in range(height):
        for j in range(width):
            if not left_set:
                return list(result_set)
            visited = [[False for i in range(width)] for j in range(height)]
            queue = []
            queue.append([[i, j], visited, board[i][j]])
            while queue:
                temp = queue.pop(0)
                word = temp[2]
                if trie.startsWith(word):
                    if trie.search(word):
                        result_set.add(word)
                        left_set.remove(word)
                    x = temp[0][1]
                    y = temp[0][0]
                    temp[1][y][x] = True
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx>=0 and nx<width and ny>=0 and ny<height:
                            if not temp[1][ny][nx]:
                                queue.append([[ny, nx], copy.deepcopy(temp[1]), word + board[ny][nx]])
    return list(result_set)

board = []
count = int(input())
for i in range(count):
    board.append(list(input().split()))
words = list(input().split())
print(findWords(board, words))