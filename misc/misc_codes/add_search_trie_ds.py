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
