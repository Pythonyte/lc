# Program to print all nodes which are at
# distance k from a leaf

# utility that allocates a new Node with
# the given val
class newNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


# Given a binary tree and a nuber k,
# print all nodes that are k distant from a leaf 
def printKDistantfromLeaf(node, k):
    MAX_HEIGHT = 10000
    path = [None] * MAX_HEIGHT
    visited = [False] * MAX_HEIGHT
    ans = []

    def kDistantFromLeafUtil(node, path, visited, pathLen, k):
        # PRE-ORDER to use feature.
        # Base case
        if (node == None):
            return

        # append this Node to the path array
        path[pathLen] = node.val
        visited[pathLen] = False

        # it's a leaf, so print the ancestor at
        # distance k only if the ancestor is
        # not already printed
        distance = pathLen - k
        if (node.left == None and node.right == None and distance >= 0 and visited[distance] == False):
            ans.append(path[distance])
            visited[distance] = True
            return

        pathLen += 1
        # If not leaf node, recur for left
        # and right subtrees
        kDistantFromLeafUtil(node.left, path, visited, pathLen, k)
        kDistantFromLeafUtil(node.right, path, visited, pathLen, k)

    kDistantFromLeafUtil(node, path, visited, 0, k)
    return ans

# Driver Code 


# Let us create binary tree given in
# the above example
# #Example 1
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.right.left.right = newNode(8)

print("Nodes at distance 2 are: {}".format(printKDistantfromLeaf(root, 2)))
print("Nodes at distance 1 are: {}".format(printKDistantfromLeaf(root, 1)))
print("Nodes at distance 0 are: {}".format(printKDistantfromLeaf(root, 0)))


#Example 2

root = newNode(1)
root.left = newNode(2)
root.left.left = newNode(4)

print("Nodes at distance 2 are: {}".format(printKDistantfromLeaf(root, 2)))
print("Nodes at distance 1 are: {}".format(printKDistantfromLeaf(root, 1)))
print("Nodes at distance 0 are: {}".format(printKDistantfromLeaf(root, 0)))