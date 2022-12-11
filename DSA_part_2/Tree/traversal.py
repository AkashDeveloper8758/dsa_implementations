from tree import Tree

def preOrderTraversal(tree:Tree):
    if tree == None:
        return
    print(tree.data,end=' ')
    preOrderTraversal(tree.left)
    preOrderTraversal(tree.right)

def postOrderTraversal(tree:Tree):
    if tree == None:
        return
    postOrderTraversal(tree.left)
    postOrderTraversal(tree.right)
    print(tree.data,end=' ')

def inOrderTraversal(tree:Tree):
    if tree == None:
        return
    inOrderTraversal(tree.left)
    print(tree.data,end=' ')
    inOrderTraversal(tree.right)

def heightOfTree(tree):
    if tree == None:
        return 0
    left = heightOfTree(tree.left)
    right = heightOfTree(tree.right)
    return max(left,right)+1

def printAtDistanceK(tree,k):
    if tree == None:
        return
    if k==0:
        print(tree.data,end=' ')
    else:
        printAtDistanceK(tree.left,k-1)
        printAtDistanceK(tree.right,k-1)

# using queue
def levelOrderTraversal(tree):
    if tree == None:
        return
    queue = []
    queue.append(tree)
    queue.append(None)
    while len(queue) > 1:
        root = queue.pop(0)
        if root == None:
            print('')
            queue.append(None)
            continue
        print(root.data,end=' ')
        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)

# using queue with inner loop
def levelOrderTraversalLineByLIne2(tree):
    if tree == None:
        return
    queue = []
    queue.append(tree)
    while len(queue) > 0:
        count = len(queue)
        for i in range(count):
            root = queue.pop(0)
            print(root.data,end=' ')
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right)
        print('')

def sizeOfBinaryTree(tree):
    if tree == None:
        return 0
    return sizeOfBinaryTree(tree.left) + sizeOfBinaryTree(tree.right)+1

def maximumInBinaryTree(tree):
    if tree == None:
        return -1
    leftmax = maximumInBinaryTree(tree.left)
    rightmax = maximumInBinaryTree(tree.right)
    return max(max(leftmax,rightmax),tree.data)

def spiralTraversal(root:Tree):
    if root == None:
        return
    queue = []
    stack = []
    queue.append(root)
    reverse = False
    while len(queue) > 0:
        count = len(queue)
        for i in range(count):
            root = queue.pop(0)
            if reverse:
                # if reverse is true, append it to stack which reverse the list otherwise print it in the correct order
                stack.append(root.data)
            else:
                print(root.data,end=' ')
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right)
        while len(stack) !=0:
            print(stack.pop(),end=' ')
        reverse = not reverse
        print('')

def spiralTraversal2(root:Tree):
    if root == None:
        return
    s1 = []
    s2 = []
    s1.append(root)
    while s1 or s2:
        while s1:
            value = s1.pop()
            print(value.data,end=' ')
            if value.left != None:
                s2.append(value.left)        
            if value.right != None:
                s2.append(value.right)
        
        while s2:
            value = s2.pop()
            print(value.data,end=' ')
            if value.right != None:
                s1.append(value.right)
            if value.left != None:
                s1.append(value.left)
     
        
                    

    


mytree = Tree(10)
mytree.left = Tree(30)
mytree.right = Tree(20)

mytree.right.left = Tree(1)
mytree.right.right = Tree(2)

mytree.left.left = Tree(3)
mytree.left.right = Tree(9)

# print('preorder : ',preOrderTraversal(mytree))
# print('inorder : ',inOrderTraversal(mytree))
# print('postorder : ',postOrderTraversal(mytree))

# print('height of tree: ',heightOfTree(mytree))
# printAtDistanceK(mytree,2)

# levelOrderTraversal(mytree)
# levelOrderTraversalLineByLIne2(mytree)
# print('size of binary tree: ',sizeOfBinaryTree(mytree))
# print('max in binary tree: ',maximumInBinaryTree(mytree))
print('max in binary tree: ')
spiralTraversal2(mytree)

#       10 
#    30------20 
#  3----9  1-----2