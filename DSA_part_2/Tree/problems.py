from tree import Tree


maxlevel = 0

# a preorder traversal
def leftViewOfTree(root,level):
    global maxlevel
    if root == None:
        return
    if maxlevel < level:
        # print the first left of that level
        print(root.data)
        maxlevel = level
    leftViewOfTree(root.left,level+1)
    leftViewOfTree(root.right,level+1)

def leftViewIterative(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while len(queue) != 0:
        count = len(queue)
        # rest of the nodes
        for i in range(count):
            # first node of this level  
            if i==0:
                print(queue[0].data)
            value = queue.pop(0)
            if value.left != None:
                queue.append(value.left)
            if value.right != None:
                queue.append(value.right)
            
def isChildrenSumProperty(root):
    if root == None or (root.left == None and root.right == None):
        return True

    childSum = 0
    if root.left != None:
        childSum+=root.left.data
        
    if root.right != None:
        childSum+=root.right.data
    
    if childSum != root.data:
        return False
    else:
        check1 = isChildrenSumProperty(root.left)
        check2 = isChildrenSumProperty(root.right)
    return check1 and check2

# if diff is more then 1 then it is unbalanced tree
def checkForHeightBalanceTree(root):
    if root==None:
        return 0
    leftHeight =checkForHeightBalanceTree(root.left)
    if leftHeight == -1:
        return -1
    rightHeight =checkForHeightBalanceTree(root.right)
    if rightHeight == -1:
        return -1
    return max(rightHeight,leftHeight)+1 if abs(rightHeight-leftHeight) <2 else -1


# similar to level order traversal, just check for the length of the queue after each level
def maxWidthOfTree(root:Tree):
    if root == None:
        return 0
    queue = []
    queue.append(root)
    res = 0
    while len(queue) != 0:
        res = max(res,len(queue))
        count = len(queue)
        for i in range(count):
            t = queue.pop(0)
            if t.left != None:
                queue.append(t.left)
            if t.right != None:
                queue.append(t.right)
    return res

prev = None
def binaryToDoublyLL(root:Tree):
    global prev
    if root == None:
        return None

    # first go for left node
    head = binaryToDoublyLL(root.left)
    if prev == None:
        # means it is first left node reach, set it to head
        head = root
    else:
        root.left = prev
        prev.next = root
    prev = root
    binaryToDoublyLL(root.right)
    return head
        
# construct a tree from preorder and inorder array
preIndex = 0
def constructFromInPre(inorder,preorder,si,ei):
    global preIndex
    if si > ei:
        return
    root = Tree(preorder[preIndex])
    preIndex +=1
    iIndex = -1
    for i in range(si,ei+1):
        if inorder[i] == root.data:
            iIndex = i 
            break
    root.left = constructFromInPre(inorder,preorder,si,iIndex-1)
    root.right = constructFromInPre(inorder,preorder,iIndex+1,ei)
    return root

def preOrderTraversal(tree:Tree):
    if tree == None:
        return
    print(tree.data,end=' ')
    preOrderTraversal(tree.left)
    preOrderTraversal(tree.right)

# diameter is the longest distance between two nodes, dia = max(dia,lh+rh+1)
# precompute height
def preComputeHeight(root,hashMap):
    if root == None:
        return 0
    lh=rh=0
    if root.left:
        lh = preComputeHeight(root.left,hashMap)
        hashMap[root.left] = lh
    if root.right:
        rh = preComputeHeight(root.right,hashMap)
        hashMap[root.right] = rh
    return max(lh,rh)+1
    

def findDiamaterFunction(root:Tree,hashmap):
    if root == None:
        return 0
    
    # d1 = 1+lh+rh
    d1 = 1
    if root.left != None:
        d1 += hashmap[root.left]
    if root.right != None:
        d1 += hashmap[root.right]
    
    d2 = findDiamaterFunction(root.left,hashmap)
    d3 = findDiamaterFunction(root.right,hashmap)
    
    return max(d1,max(d2,d3))

def findDiameter(root:Tree):
    hashmap = {}
    preComputeHeight(root,hashmap)
    dia = findDiamaterFunction(root,hashmap)
    return dia


# find diamater efficient ----------------------------
maxDia = 0
def findDiaEfficient(root):
    global maxDia
    if root == None:
        return 0

    lh = findDiaEfficient(root.left)
    rh = findDiaEfficient(root.right)
    maxDia = max(maxDia,lh+rh+1)
    return max(lh,rh)+1
    


mytree = Tree(50)

mytree.right = Tree(20)
mytree.right.left = Tree(10)
mytree.right.right = Tree(10)

mytree.left = Tree(30)
mytree.left.left = Tree(21)
mytree.left.right = Tree(9)
mytree.left.right.left = Tree(4)

# newTree = constructFromInPre([20,10,40,30,50],[10,20,30,40,50],0,4)
# preOrderTraversal(newTree)

# print('find diamater : ',findDiameter(mytree))
findDiaEfficient(mytree)
print('find diamater : ',maxDia)
#       10 
#    30------20 
#  3----9  1-----2
#    -4-
# leftViewIterative(mytree)
# print('is children sum pro: ',isChildrenSumProperty(mytree))
# print('check for height balance : ',checkForHeightBalanceTree(mytree))
# print('max width of tree : ',maxWidthOfTree(mytree))
