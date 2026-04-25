class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, index):
            # If we reached end of word
            if index == len(word):
                return node.is_end

            ch = word[index]

            # If character is not '.'
            if ch != '.':
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], index + 1)

            # If character is '.', try all possibilities
            for child in node.children.values():
                if dfs(child, index + 1):
                    return True

            return False

        return dfs(self.root, 0)