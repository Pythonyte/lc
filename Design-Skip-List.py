# https://www.geeksforgeeks.org/skip-list/
# https://leetcode.com/problems/design-skiplist/discuss/394679/Python-the-%22down%22-pointer-of-each-node-must-point-to-node-of-same-value-in-the-next-level
# https://leetcode.com/problems/design-skiplist/description/

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.down=None

class Skiplist:
      
    def __init__(self):
        self.levels=[]
        prev=None
        for i in range(16):
            node=Node(-math.inf)
            self.levels.append(node)
            if prev:
                prev.down=node
            prev=node
			
    def _iter(self,val):
        res=[]
        l=self.levels[0]
        while l:
            while l.next and l.next.val<val:
                l=l.next
            res.append(l)
            l=l.down
        return res
		
    def search(self, target: int) -> bool:
        last=self._iter(target)[-1]
        return last.next and last.next.val==target
		
    def add(self, num: int) -> None:
        res=self._iter(num)
        prev=None
        for i in range(len(res)-1,-1,-1):
            node=Node(num)
            node.next,node.down=res[i].next,prev
            res[i].next=node
            prev=node
            rand=random.random()
            if rand>0.5:
                break
				
    def erase(self, num: int) -> bool:
        found=False
        res=self._iter(num)
        for i in range(len(res)):
            if res[i].next and res[i].next.val==num:
                res[i].next=res[i].next.next
                found=True
        return found

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
