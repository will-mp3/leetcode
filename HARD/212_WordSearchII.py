"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
 
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

"""
to solve this problem effeciently we will make use of a trie (prefix tree) data structure.
the basic logic of the tree is each node will have a dictionary of children, this will allow us to quickly acces which children it may have.
the reason this is necesary is each node can have up to 26 children, lowercase a-z.
when we create a node we also give it a variable isWord to track if its the end of a word, useful later.
to insert a word we check to see if the current character is a child of our current node, if not we create a new node for that character.
once the entire word has been added, using existing nodes or new nodes, we set its last character nodes endOfWord variable to True.
we start by adding all of the words in our word list to this trie structure for future access.
using this, we create a dfs function to go through the entire matrix of characters.
we first check if the character is valid, its inbounds and the character is in the children set for our node.
if this is true we add it to our visit set, update the node to this child, add the character to our word string, and check isWord.
if this is the end of the word, we add the word string to result. 
then call the dfs function on the every direction from our current node.
once this is finished executing we remove the cell from our visit set.
outside of the dfs function we create a nested loop going through every cell in our matric, calling dfs on every position.
when this is finished running we return our list of words.
"""