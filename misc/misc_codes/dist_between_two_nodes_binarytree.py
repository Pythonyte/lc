"""
A python program to find distance between n1
and n2 in binary tree
"""


# binary tree node
class Node:
    # Constructor to create new node
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


# This function returns pointer to LCA of
# two given values n1 and n2.
def LCA(root, n1, n2):
    if root is None: return None
    if root.val == n1 or root.val == n2: return root
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)
    if left and right:
        return root
    return left if left else right

def findLevel(root, data):
    # Base case
    if (root == None):
        return -1

    # Initialize distance
    dist = -1

    # Check if x is present at root or
    # in left subtree or right subtree.
    if (root.val == data):
        return dist + 1
    else:
        dist = findLevel(root.left, data)
        if dist >= 0:
            return dist + 1
        else:
            dist = findLevel(root.right, data)
            if dist >= 0:
                return dist + 1

    return dist


# function to find distance between two
# nodes in a binary tree
def findDistance(root, n1, n2):
    lca = LCA(root, n1, n2)
    # if lca exist
    if lca:

        # distance of n1 from lca
        d1 = findLevel(lca, n1)

        # distance of n2 from lca
        d2 = findLevel(lca, n2)
        return d1 + d2
    else:
        return -1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print("Dist(4,5) = ", findDistance(root, 4, 5))
print("Dist(4,6) = ", findDistance(root, 4, 6))
print("Dist(3,4) = ", findDistance(root, 3, 4))
print("Dist(2,4) = ", findDistance(root, 2, 4))
print("Dist(8,5) = ", findDistance(root, 8, 5))