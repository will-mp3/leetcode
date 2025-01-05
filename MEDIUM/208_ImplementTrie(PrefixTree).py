"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children: # check if character is in our hashmap
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        # whether we already had the nodes or had to create them, cur is now the last letter in the word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        # this loop continues for every character until we find one that dosent exist or we reach then end of the word
        return cur.endOfWord # we can only return true if this fina character is the end of a word

    def startsWith(self, prefix: str) -> bool:
        # this method is exactly the same as search, except it dosent matter if the final character is the end of the word
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True

"""
a trie is a form of tree that handles strings, and specifically their prefixes.
our trie needs to be able to insert words, search for words, and search for prefixes.
the basic logic of the tree is each node will have a dictionary of children, this will allow us to quickly acces which children it may have.
the reason this is necesary is each node can have up to 26 children, lowercase a-z.
when we create a node we also give it a variable endOfWord to track if its the end of a word, useful later.
to insert a word we check to see if the current character is a child of our current node, if not we create a new node for that character.
once the entire word has been added, using existing nodes or new nodes, we set its last character nodes endOfWord variable to True.
to search for a word we begin at the root and check the children for our current letter, if it is ever not present we return false.
if the current letter is present we set cur equal to that node and continue.
this checks to see if we have all the letters present in order, in our tree.
once finished we have to last check if that final character is marked as the end of the word.
the startsWith function, or prefix search, has identical logic to search except it dosent check for endOfWord.
"""