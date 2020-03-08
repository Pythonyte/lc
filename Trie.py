class TrieNode():
    def __init__(self):
        self.children = [None]*123
        self.isWord = False

class Trie:
    """
    insert => man
    root = [,,,Tm,,,] False
    Tm = [,,Ta,,,] False
    Ta = [,,Tn,,,] False
    Tn = [,,,,,,] True

    insert mask:
    root = [,,,Tm,,,] False
    Tm = [,,Ta,,,] False
    Ta = [,,Tn,,Ts,,,] False
    Tn = [,,,,,,] True
    Ts = [,,,,,Tk...] False
    Tk = [,,,,] True

    """
    def __init__(self):
        self.root = TrieNode()

    def printTrie(self, node=None, space=" "):
        node = self.root if not node else node
        for idx, tnode in enumerate(node.children):
            if tnode:
                # Printing tnode's isword because, at idx index of children array, there is tnode
                # which is actually Trinode for chr(idx)
                print("{} {} {}".format(space, chr(idx), tnode.isWord))
                self.printTrie(tnode, space + " ")

    def add_word(self, word):
        if not word: return True
        node = self.root
        for w in word:
            idx = ord(w)
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isWord = True

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
        else:
            node = node.children[ord(word[0])]
            if not node:
                return
            self.dfs(node, word[1:])

    def search_word(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res


t = Trie()
t.add_word("man")
t.add_word("mango")
t.add_word("matter")
t.add_word("smit")
t.add_word("monday")
t.printTrie()
print(t.search_word('mango'))
print(t.search_word('msss'))