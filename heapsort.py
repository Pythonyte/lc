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
    
    def oldheappop(self):

        if not self.heapsize: return None
        popped_item =  self.heapq[1]
        # Normal Implementation
        self.heapq[1] = self.heapq[self.heapsize]
        self.heapq.pop()

        # Extra Ordinary Implementation,
        # By this way WE are pushing popped max item into heap last empty space, then second last empty space
        # and so on
        # self.heapq[1], self.heapq[self.heapsize] = self.heapq[self.heapsize], self.heapq[1]
        # This will not impact in our code becuase we are always maintaining heapsize, so out of scroped elements
        # will never get encounterd in normal process
        self.heapsize -= 1
        self.shiftdown()
        return popped_item
        
    def heappop(self):

        if not self.heapsize: return None
        popped_item = self.heapq[1]
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
        return popped_item

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

def heapsort_v1(nums):
    heap = maxheap()
    for num in nums:
        heap.heappush(num)
    output = [None]*heap.heapsize
    while heap.heapsize:
        output[heap.heapsize] = heap.oldheappop()
    return output

def heapsort_v2(nums):
    heap = maxheap()
    for num in nums:
        heap.heappush(num)
    while heap.heapsize:
        heap.heappop()
    return heap.heapq[1:]

def heapsort_v3(nums):
    """
    1. Create a min heap for given array (nlogn)
    2. pop from heap and append into output (nlogn for popping n elements)
    :param nums:
    :return:
    """
    import heapq
    heapq.heapify(nums)
    output = []
    while nums:
        output.append(heapq.heappop(nums))
    return output


print(heapsort_v1([2,-3]))
print(heapsort_v1([0]))
print(heapsort_v1([9,8,12,6,-9]))
print(heapsort_v1([8,8,8,8]))
print(heapsort_v1([-9,-9,-9,-12]))
print(heapsort_v1([0,1,2,3,3,4]))
print(heapsort_v1([9,8,7,6,5,4,3]))


print(heapsort_v3([2,-3]))
print(heapsort_v3([0]))
print(heapsort_v3([9,8,12,6,-9]))
print(heapsort_v3([8,8,8,8]))
print(heapsort_v3([-9,-9,-9,-12]))
print(heapsort_v3([0,1,2,3,3,4]))
print(heapsort_v3([9,8,7,6,5,4,3]))


print(heapsort_v2([2,-3]))
print(heapsort_v2([0]))
print(heapsort_v2([9,8,12,6,-9]))
print(heapsort_v2([8,8,8,8]))
print(heapsort_v2([-9,-9,-9,-12]))
print(heapsort_v2([0,1,2,3,3,4]))
print(heapsort_v2([9,8,7,6,5,4,3]))
