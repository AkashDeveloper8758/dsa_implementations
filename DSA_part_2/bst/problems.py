from tree import Tree,levelTraversal
from sortedcontainers import SortedDict
import math

def itemsToBeSwapped(arr:list):
    first = second = None
    prev = -math.inf
    for i in range(len(arr)):
        if arr[i] < prev:
            if first == None:
                first = prev
            second = arr[i]
        prev = arr[i]
    return [first,second]

# similar to array implementation
first = second = prev = None
def twoSwappedBST(root:Tree):
    global first,second,prev
    if root == None:
        return None
    # go left
    twoSwappedBST(root.left)
    # check for root
    if prev != None and prev.data >root.data:
        if first == None:
            first = prev
        second = root
    prev = root
    twoSwappedBST(root.right)

# using hashing
def pairSumInBst(root:Tree,sumv,hashSet = set()):
    if root == None:
        return False
    # if found in left, return
    if pairSumInBst(root.left,sumv,hashSet):
        return True
    if sumv - root.data in hashSet:
        return True
    else:
        hashSet.add(root.data)
    return pairSumInBst(root.right,sumv,hashSet)

# inorder traversal
def verticalSum(root:Tree,level = 0,sortedMap = SortedDict()):
    if root == None:
        return
    verticalSum(root.left,level-1,sortedMap)
    if level in sortedMap:
        sortedMap[level]+=root.data
    else:
        sortedMap[level] = root.data
    verticalSum(root.right,level+1,sortedMap)
    return sortedMap

# ------------ iterative solution of vertical traversal -----------------
class Pair:
    def __init__(self,tree:Tree,hd):
        self.node = tree
        self.hd = hd

def verticalTraversalIterative(root:Tree):
    if root == None:
        return
    queue = []
    sortedMap = SortedDict()
    queue.append(Pair(root,0))
    while len(queue) != 0:
        value:Pair = queue.pop(0)
        nodev = value.node
        hdv = value.hd
        if hdv in sortedMap:
            sortedMap[hdv].append(nodev)
        else:
            sortedMap[hdv] = [nodev]
        if nodev.left != None:
            queue.append(Pair(nodev.left,hdv-1))
        if nodev.right != None:
            queue.append(Pair(nodev.right,hdv+1))

    for values in sortedMap.values():
        for v in values:
            print(v.data,end=' ')
        print('')

# without the use of sortedDict
def verticalOrderIterative_eff(root): 
    #Your code here
    minHd = 0
    maxHd = 0
    queue = []
    
    hd = {}
    hashMap = {}
    
    res = []
    queue.append(root)
    hd[root] = 0
    hashMap[0] = [root.data]
    while queue:
        r = queue.pop(0)
        if r.left != None:
            queue.append(r.left)
            hd[r.left] = hd[r]-1
            minHd = min(minHd,hd[r.left])
            if hd[r.left] in hashMap:
                hashMap[hd[r.left]].append(r.left.data)
            else:
                hashMap[hd[r.left]] = [r.left.data]
        
        if r.right != None:
            queue.append(r.right)
            hd[r.right] = hd[r]+1
            maxHd = max(maxHd,hd[r.right])
            if hd[r.right] in hashMap:
                hashMap[hd[r.right]].append(r.right.data)
            else:
                hashMap[hd[r.right]] = [r.right.data]
    for i in range(minHd,maxHd+1):
        res.extend(hashMap[i])
    return res
# traversal : level order
def topViewOfTree(root:Tree):
    if root == None:
        return
    queue = []
    sortedMap = SortedDict()
    queue.append(Pair(root,0))
    while len(queue) != 0:
        value:Pair = queue.pop(0)
        nodev = value.node
        hdv = value.hd
        if hdv not in sortedMap:
            sortedMap[hdv] = nodev
        
        if nodev.left != None:
            queue.append(Pair(nodev.left,hdv-1))
        if nodev.right != None:
            queue.append(Pair(nodev.right,hdv+1))
    return sortedMap
    
def bottomViewOfTree(root:Tree):
    if root == None:
        return
    queue = []
    sortedMap = SortedDict()
    queue.append(Pair(root,0))
    while len(queue) != 0:
        value:Pair = queue.pop(0)
        nodev = value.node
        hdv = value.hd
        
        sortedMap[hdv] = nodev
        
        if nodev.left != None:
            queue.append(Pair(nodev.left,hdv-1))
        if nodev.right != None:
            queue.append(Pair(nodev.right,hdv+1))
    return sortedMap
    
# -------------- top view of binary tree -----------
# iterative solution using pair class

# def topView(root:Tree):
#     if root == None:
#         return None
#     queue = []
#     sortedMap = SortedDict()
#     queue.append(Pair(root,0))
#     while len(queue) != 0:
#         value:Pair = queue.pop(0)
#         node = value.node
#         hd = value.hd
#         if 



mytree = Tree(12)
mytree.left = Tree(8)
mytree.right = Tree(20)

mytree.right.left = Tree(15)
mytree.right.right = Tree(25)

mytree.left.left = Tree(5)
mytree.left.right = Tree(9)
mytree.left.right.right = Tree(10)

currLev = -1
def LeftView(root,level = 0,res = []):
    global currLev
    if root == None:
        return
    print(currLev)
    if currLev < level:
        currLev = level
        res.append(root.data)
    LeftView(root.left,level+1,res)
    LeftView(root.right,level+1,res)
    return res

print('leftview of bt: ',LeftView(mytree))


#        12 
#     8------20
#  5----9  15----25

# print('items to be swapped : ',itemsToBeSwapped([1,5,3,4,2,6,7]))
# twoSwappedBST(mytree)
# if first != None:
#     print('first : ',first.data)
# if second != None:
#     print('second: ',second.data)

# print('is parisum is present : ',pairSumInBst(mytree,41))
# print('vertical sum : ',list(verticalSum(mytree).values()))
# verticalTraversalIterative(mytree)
# print('top view of binary tree : ',[x.data for x in list(topViewOfTree(mytree).values())])
# print('bottom view of binary tree : ',[x.data for x in list(bottomViewOfTree(mytree).values())])