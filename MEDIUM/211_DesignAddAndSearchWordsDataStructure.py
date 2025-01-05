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

                # dot handling
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child): # skipping the dot so increment i + 1
                            return True
                    return False # if we never find a match return false
                
                # standard handling
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.endOfWord
        
        return dfs(0, self.root)

"""
to solve this problem we will use a trie, or prefix tree, data structure (see leetcode 208).
the basic logic of the tree is each node will have a dictionary of children, this will allow us to quickly acces which children it may have.
the reason this is necesary is each node can have up to 26 children, lowercase a-z.
when we create a node we also give it a variable endOfWord to track if its the end of a word, useful later.
to insert a word we check to see if the current character is a child of our current node, if not we create a new node for that character.
once the entire word has been added, using existing nodes or new nodes, we set its last character nodes endOfWord variable to True.
this problem has a tricky case in the "." character, which acts as a sort of wildcard.
to handle this we will make use of a recursive dfs function, since our dot needs to be checked with every child available.
if a dot is present we go through all of the children of our current node, running our dfs funciton on them until we find our word.
if we do not find the word, True is not returned, we exit the loop and return False.
this recursive handling is only necesary in the even a dot is present, otherwise the standard search logic applies.
to search for a word we begin at the root and check the children for our current letter, if it is ever not present we return false.
if the current letter is present we set cur equal to that node and continue.
this checks to see if we have all the letters present in order, in our tree.
once finished we have to last check if that final character is marked as the end of the word.
"""