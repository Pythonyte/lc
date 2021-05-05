https://www.geeksforgeeks.org/print-nodes-distance-k-leaf-node/
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

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################

# Function to check if a given node is a leaf node or not
def isLeaf(node):
    return node.left is None and node.right is None


# Recursive function to find all nodes at a given distance from leaf nodes
def leafNodeDistance(node, path, set, dist):
    # base case: empty tree
    if node is None:
        return

    # if a leaf node is found, insert the node at a distance `dist` from the
    # leaf node into the set
    if isLeaf(node) and len(path) >= dist:
        set.add(path[-dist])
        return

    # include the current node in the current path
    path.append(node)
    # recur for the left and right subtree
    leafNodeDistance(node.left, path, set, dist)
    leafNodeDistance(node.right, path, set, dist)

    # remove the current node from the current path
    path.remove(node)


# Find all distinct nodes at a given distance from leaf nodes
def printLeafNodeDistance(node, dist):
    # list to store root-to-leaf path
    path = []

    # create an empty set to store distinct nodes at a given
    # distance from leaf nodes
    s = set()

    # find all nodes
    leafNodeDistance(node, path, s, dist)

    # print output
    print([e.val for e in s])

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
