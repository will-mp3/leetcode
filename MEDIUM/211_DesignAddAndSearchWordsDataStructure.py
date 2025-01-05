"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children: # check if character is in our hashmap
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        # whether we already had the nodes or had to create them, cur is now the last letter in the word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child): # skipping the dot so increment i + 1
                            return True
                    return False # if we never find a match return false
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.endOfWord
        
        return dfs(0, self.root)

"""

"""