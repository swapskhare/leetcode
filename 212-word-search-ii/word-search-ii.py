class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for w in words:
            root.add(w)

        ROWS, COLS = len(board), len(board[0])
        ans = set()
        visited = set()

        def backtrack(r, c, node, currword):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] not in node.children):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            currword += board[r][c]
            if node.end:
                ans.add(currword)

            backtrack(r + 1, c, node, currword)
            backtrack(r - 1, c, node, currword)
            backtrack(r , c + 1, node, currword)
            backtrack(r, c - 1, node, currword)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")

        return list(ans)


