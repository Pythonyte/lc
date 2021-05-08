"""
50.  Design Range set data structure which support 2 operations – AddInRangeSet and SearchInRangeSet
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
"""
#################### MORE OPTIMIZED SOLUTION #############################
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False
    
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        if not word: 
            return Node
        node = self.root
        for w in word:
            node = node.children[w]
        node.isword = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            if not word:
                if node.isword:
                    nonlocal res
                    res = True
                return
            
            char = word[0]     
            if word[0] == '.':
                for child in node.children.values():
                    dfs(child, word[1:])
            else:
                node = node.children.get(char)
                if not node:
                    return
                dfs(node, word[1:])
            
        res = False
        dfs(self.root, word)
        return res
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


#####################################################################################
#####################################################################################



class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def printTrie(self, node=None, space=" "):
        node = self.root if not node else node
        for key, tnode in node.children.items():
            print("{} {} {}".format(space, key, node.isWord))
            self.printTrie(tnode, space + " ")

    def addWord(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])

wd = WordDictionary()
wd.addWord('sumit')
wd.addWord('surfing')
wd.printTrie()
print('s..it', wd.search('s..it'))



##### OPTIMIZED 210321
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isword = True

    def dfs(self, node, word, resultent):
        if not word:
            if node.isword:
                self.res.append(resultent)
                return
        if word[0] == '.':
            for key, tnode in node.children.items():
                self.dfs(tnode, word[1:], resultent+key)
        elif word[0] in node.children:
            tnode = node.children[word[0]]
            self.dfs(tnode, word[1:], resultent+word[0])

    def search(self, word):
        node = self.root
        self.res = []
        self.dfs(node, word, '')
        return self.res

    def print_trie(self, space="", node=None):
        node = self.root if not node else node
        for char, tnode, in node.children.items():
            is_word = '*' if tnode.isword else ''
            print(space, char, is_word)
            self.print_trie(space + " ", tnode)

wd = WordDictionary()
wd.add_word('sumit')
wd.add_word('ramit')
wd.add_word('sameer')
wd.print_trie()
print(wd.search('..mit'))
print(wd.search('..mee.'))
print(wd.search('..mat'))


### Output
 s 
  u 
   m 
    i 
     t *
  a 
   m 
    e 
     e 
      r *
 r 
  a 
   m 
    i 
     t *
['sumit', 'ramit']
['sameer']
[]
