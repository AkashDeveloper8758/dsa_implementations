import math
from tree import Tree,preOrderTraversal

# create path to the node
def pathFinder(root:Tree,node,array):
    if root == None:
        return False
    array.append(root)
    if root.data == node:
        return True
    # if any side contain node, return true
    if pathFinder(root.left,node,array) or pathFinder(root.right,node,array):
        return True
    # else remove the last node
    array.pop()
    return False

# lowest common ancester
def findLCA(root:Tree,n1,n2):
    array1 = []
    array2 = []
    # if any of the path return false, means any node does not exist in the tree 
    if not pathFinder(root,n1,array1) or not pathFinder(root,n2,array2):
        return None
    i=0
    lastOcc = None
    while i<len(array1) and i<len(array2):
        if array1[i] and array2[i] and array1[i] == array2[i]:
            lastOcc = array1[i].data
            i+=1
        else:
            return lastOcc
    return lastOcc

# find lca efficient, assuming nodes present in the tree
def findLCAEff(root:Tree,n1,n2):
    if root == None:
        return None
    # if root is same as any of the key
    if root.data == n1 or root.data == n2:
        return root
    lca1 = findLCAEff(root.left,n1,n2)
    lca2 = findLCAEff(root.right,n1,n2)
    # if both are not none means this is the parent whose left and right contain nodes
    if lca1 != None and lca2 != None:
        return root
    if lca1:
        return lca1
    else:
        return lca2

# ---------- burn tree ---------
# idea: every node has two measure: height, distance from given leaf
#       if leaf is not an descendent of the node, then distance from leaf is set to -1
#       else distance = 0 and it is passed by reference so it is updated by childs to the parent
class Distance:
    def __init__(self,val):
        self.val = val
# here distance is passed by reference, means it can be changed by childs calls
# this function return height
burnRes = 0
def burnTree(root:Tree,leaf:Tree,dis:Distance):
    global burnRes
    if root == None:
        return 0
    if root == leaf:
        # if root is leaf, then set dis = 0
        dis.val = 0
        return 1
    ldis = Distance(-1)
    rdis = Distance(-1)
    lheight = burnTree(root.left,leaf,ldis)
    rheight = burnTree(root.right,leaf,rdis)
    # means leaf present in left node somewhere
    if ldis != -1:
        dis.val = ldis.val+1


        # if leaf is in ldis, and we have left dis, to find total add right height, resp. for right != -1
        burnRes = max(burnRes,dis.val+rheight)
    elif rdis != -1:
        dis.val = rdis.val+1
        burnRes = max(burnRes,dis.val+lheight)
    return max(lheight,rheight)+1

# ----------- count nodes in complete binary tree -------------
# naive: time-> O(n)
def countNodesInCompleteBT(root:Tree):
    if root == None:
        return 0
    lh = countNodesInCompleteBT(root.left)
    rh = countNodesInCompleteBT(root.right)
    return lh+rh+1
# efficient
# time : O(logn*long)
def countNodeInCompleteBST_eff(root:Tree):
    if root == None:
        return 0
    lh = rh  =0
    curr = root
    # count left-left
    while curr!= None:
        lh+=1
        curr = curr.left

    # count right-right
    curr = root
    while curr!= None:
        rh+=1
        curr = curr.right

    if lh == rh:
        return math.pow(2,lh)-1
    else:
        return  countNodeInCompleteBST_eff(root.left) + countNodeInCompleteBST_eff(root.right) + 1

def serializeBinaryTree(root:Tree,arr=[]):
    if root == None:
        arr.append(-1)
        return arr
    arr.append(root.data)
    serializeBinaryTree(root.left,arr)
    serializeBinaryTree(root.right,arr)
    return arr

bt_index= 0
def deserializeBT(arr):
    global bt_index
    if bt_index == len(arr):
        return None
    value = arr[bt_index]
    bt_index+=1
    if value != -1:
        root = Tree(value)
        root.left = deserializeBT(arr)
        root.right = deserializeBT(arr)
        return root
    else:
        return None

def iterativeInorder(root:Tree):
    if root == None:
        return None
    stack = []
    curr = root
    while curr != None or len(stack) != 0:
        while curr:
            # go to left-left
            stack.append(curr)
            curr = curr.left
        # print the leftmost and pop from the stack
        curr = stack.pop()
        print(curr.data,end=' ')
        # go to the right and repeat the same process
        curr = curr.right

def iterativePreOrder(root:Tree):
    if root == None:
        return 
    stack = []
    stack.append(root)
    while len(stack) != 0:
        curr = stack.pop()
        print(curr.data,end=' ')
        if curr.right != None:
            stack.append(curr.right)
        if curr.left != None:
            stack.append(curr.left)
# space : O(h)
# idea=> we are anyways going to left, so only store right element to process them later and continue printing left
def iterativePreorderEff(root:Tree):
    if root == None:
        return 
    stack = []
    curr = root
    while len(stack) != 0 or curr!= None:
        while curr:
            print(curr.data,end=' ')
            if curr.right != None:
                stack.append(curr.right)
            curr = curr.left
        if len(stack) != 0:
            curr = stack.pop()

mytree = Tree(10)

mytree.left = Tree(30)
mytree.right = Tree(20)

mytree.right.left = Tree(1)
mytree.right.right = Tree(2)

mytree.left.left = Tree(3)
mytree.left.right = Tree(9)

# mytree.left.left.left = Tree(11)
# mytree.left.left.right = Tree(14)

#       10
#    30------20 
#  3----9  1-----2

# print('least common ansester is : ',findLCAEff(mytree,30,1).data)
# burnTree(mytree,mytree.left.right.right,Distance(-1))
# print('time take to burn tree : ',burnRes)
# print('nodes in complete binary tree: ',countNodesInCompleteBT(mytree))
# print('nodes in complete binary tree (eff): ',countNodeInCompleteBST_eff(mytree))

# ---------------------- seralization and desirilizatin -------------------

# print('before serilization : ')
# preOrderTraversal(mytree)
# print('')
# print('after serilization : ')
# btArr = serializeBinaryTree(mytree)
# for i in btArr:
#     print(i,end=' ')

# print('')
# print('after Deserialization : ')
# btRoot = deserializeBT(btArr)
# preOrderTraversal(btRoot)

# ---------------------- seralization and desirilizatin -------------------
# print('serilized binary tree: ',serializeBinaryTree(mytree))
# iterativeInorder(mytree)
print('')
# iterativePreOrder(mytree)
iterativePreorderEff(mytree)
