# Python3 implementation to check if the
# given array can represent Level Order
# Traversal of Binary Search Tree
INT_MIN, INT_MAX = float('-inf'), float('inf')


# To store details of a node like node's
# data, 'min' and 'max' to obtain the
# range of values where node's left
# and right child's should lie
class NodeDetails:

    def __init__(self, data, min, max):
        self.data = data
        self.min = min
        self.max = max


# function to check if the given array
# can represent Level Order Traversal
# of Binary Search Tree
def levelOrderIsOfBST(arr, n):
    # if tree is empty
    if n == 0:
        return True

    # queue to store NodeDetails
    q = []

    # index variable to access array elements
    i = 0

    # node details for the root of the BST
    newNode = NodeDetails(arr[i], INT_MIN, INT_MAX)
    i += 1
    q.append(newNode)

    # until there are no more elements
    # in arr[] or queue is not empty
    while i != n and len(q) != 0:

        # extracting NodeDetails of a
        # node from the queue
        temp = q.pop(0)
        print("1===>",i,temp.data, temp.min, temp.max)
        # check whether there are more elements
        # in the arr[] and arr[i] can be left
        # child of 'temp.data' or not
        if i < n and (arr[i] < temp.data and
                      arr[i] > temp.min):
            # Create NodeDetails for newNode
            # / and add it to the queue
            newNode = NodeDetails(arr[i], temp.min, temp.data)
            i += 1
            q.append(newNode)
        print("2===>", i, temp.data, temp.min, temp.max)
        # check whether there are more elements
        # in the arr[] and arr[i] can be right
        # child of 'temp.data' or not
        if i < n and (arr[i] > temp.data and
                      arr[i] < temp.max):
            # Create NodeDetails for newNode
            # / and add it to the queue
            newNode = NodeDetails(arr[i], temp.data, temp.max)
            i += 1
            q.append(newNode)

            # given array represents level
    # order traversal of BST
    if i == n:
        return True

    # given array do not represent
    # level order traversal of BST
    return False


# Driver code
if __name__ == "__main__":

    arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    n = len(arr)
    if levelOrderIsOfBST(arr, n):
        print("Yes")
    else:
        print("No")
