class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""


class Solution:
    def findWords(self, board, words):
        # Build Trie
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return

            next_node = node.children[char]

            # Found word
            if next_node.word:
                result.append(next_node.word)
                next_node.word = ""   # Avoid duplicates

            # Mark visited
            board[r][c] = "#"

            # 4 directions
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            # Restore
            board[r][c] = char

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result