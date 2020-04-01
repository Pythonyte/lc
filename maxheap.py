class maxheap:
    def __init__(self):
        self.heapq = [0]
        self.heapsize = 0

    def __str__(self):
        return " ".join([str(x) for x in self.heapq[1:self.heapsize+1]])

    def heappush(self, item):
        self.heapq.append(item)
        self.heapsize += 1
        self.shiftup()

    def shiftup(self):
        parent, child = self.heapsize // 2, self.heapsize
        while parent and self.heapq[parent] < self.heapq[child]:
            self.heapq[parent], self.heapq[child] = self.heapq[child], self.heapq[parent]
            child =  child // 2
            parent = parent // 2

    def top(self):
        if self.heapsize:
            return self.heapq[1]
        else:
            return None

    def heappop(self):
        
        if not self.heapsize: return None
        
        # Normal Implementation
        # self.heapq[1] = self.heapq[self.heapsize]
        # self.heapq.pop()
        
        # Extra Ordinary Implementation, 
        # By this way WE are pushing popped max item into heap last empty space, then second last empty space 
        # and so on
        self.heapq[1], self.heapq[self.heapsize] = self.heapq[self.heapsize], self.heapq[1]
        # This will not impact in our code becuase we are always maintaining heapsize, so out of scroped elements
        # will never get encounterd in normal process
        self.heapsize -= 1
        self.shiftdown()

    def get_bigger_child(self, parent=1):
        lchild = 2 * parent
        rchild = 2 * parent + 1

        # if heaplist is lesser than lchild, means no child exists for that parent
        if self.heapsize < lchild:
            return None

        # if heaplist is lesser than rchild, means left chlid is smallest
        if self.heapsize < rchild:
            return lchild

        # if both childs exists then figure out maximum one
        if self.heapq[lchild] < self.heapq[rchild]:
            return rchild
        else:
            return lchild


    def shiftdown(self):
        parent = 1
        while parent*2 <= self.heapsize:
            child = self.get_bigger_child(parent=parent)
            if self.heapq[child] > self.heapq[parent]:
                self.heapq[parent], self.heapq[child] = self.heapq[child], self.heapq[parent]
                parent = child
            else:
                return




mh = maxheap()
mh.heappush(10)
mh.heappush(20)
mh.heappush(5)
mh.heappush(34)
print(mh)
mh.heappop()
mh.heappop()
mh.heappop()
print(mh)

print("Removed Elements are present in elemenated portion of heap: HeapSort",mh.heapq[mh.heapsize+1:])

# Output
Heap 34 20 5 10
Heap 5
Removed Elements are present in elemenated portion of heap: HeapSort [10, 20, 34]
