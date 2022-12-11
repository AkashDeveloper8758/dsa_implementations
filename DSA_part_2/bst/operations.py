from tree import Tree,levelTraversal
# from sortedcontainers import SortedList, SortedSet, SortedDict
import math
# recursive
def searchInBST(root:Tree,ele):
    if root == None:
        return False
    if root.data == ele:
        return True
    if root.data > ele:
        return searchInBST(root.left,ele)
    else:
        return searchInBST(root.right,ele)

# iterative
def searchInBSTiterative(root:Tree,ele):
    while root != None:
        if root.data == ele:
            return True
        if root.data > ele:
            root = root.left
        else:
            root = root.right
    return False

# this iterative will save O(h) call stack
def insertInBST(root:Tree,ele):
    newNode = Tree(ele)
    if root == None:
        return newNode
    currRoot = root
    pre = None
    while root != None:
        pre = root
        if root.data > ele:
            root = root.left
        elif root.data < ele:
            root = root.right
        else:
            return currRoot

    if ele < pre.data:
        pre.left= newNode
    else:
        pre.right = newNode
    return currRoot

def insertRecursive(root:Tree,ele):
    if root == None:
        return Tree(ele)
    if ele < root.data:
        root.left = insertRecursive(root.left,ele)
    elif ele > root.data:
        root.right= insertRecursive(root.right,ele)
    return root

# find closest greater eleemnt: go to left-left in right child
def findSucc(root:Tree):
    curr = root.right
    while curr!= None and curr.left != None:
        curr = curr.left
    return curr


def deleteInBST(root:Tree,ele):
    if root == None:
        return None
    if ele < root.data:
        root.left = deleteInBST(root.left,ele)
    elif ele > root.data:
        root.right = deleteInBST(root.right,ele)
    else:
        # if delete node is found
        # if has only one child, return the other
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            # if both are there
            # find successor on right side to replace with
            # findSucc => left most element in right child
            succ = findSucc(root)
            root.data = succ.data
            # delete the succ in the bst
            root.right = deleteInBST(root.right,succ.data)
        return root
    return root

def findFloor(root:Tree,value):
    if root == None:
        return None
    curr = root
    res = None
    while curr != None:
        # case 1
        if curr.data == value:
            return curr.data
        # case 2
        if curr.data > value:
            curr = curr.left
        else:
            res = curr.data
            curr = curr.right
    return res

def findCeil(root:Tree,value):
    if root == None:
        return None
    res = None
    while root != None:
        if root.data == value:
            return root.data
        if root.data > value:
            res = root.data
            root = root.left
        else:
            root = root.right
    return res

def isBST(root:Tree,lower=-math.inf,upper=math.inf):
    if root == None:
        return True
    return root.data > lower and root.data < upper and isBST(root.left,lower,root.data) and isBST(root.right,root.data,upper)


# idea : inorder traversal is always sorted
prevSort = -math.inf
def isBST2(root:Tree):
    global prevSort
    if root == None:
        return True
    if not isBST2(root.left):
        return False
    if root.data <= prevSort:
        return False
    prevSort = root.data
    return isBST2(root.right)
    

mytree = Tree(12)
mytree.left = Tree(8)
mytree.right = Tree(20)

mytree.right.left = Tree(10)
mytree.right.right = Tree(25)

mytree.left.left = Tree(5)
mytree.left.right = Tree(9)

# print('search in BST : ',searchInBSTiterative(mytree,15))
# mytree = insertInBST(mytree,32)
# mytree = insertInBST(mytree,45)
# mytree = insertInBST(mytree,15)
# mytree = insertInBST(mytree,12)
# mytree = insertRecursive(mytree,8)
# mytree = insertRecursive(mytree,2)
# mytree = insertRecursive(mytree,1)
# mytree = insertRecursive(mytree,9)

levelTraversal(mytree)
# mytree = deleteInBST(mytree,12)
# print('find floor : ',findFloor(mytree,10))
# print('find ceil : ',findCeil(mytree,46))
print('is bst : ',isBST2(mytree))

