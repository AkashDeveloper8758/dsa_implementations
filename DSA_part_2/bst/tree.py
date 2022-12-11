class Tree:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        
def preOrderTraversal(tree:Tree):
    if tree == None:
        return
    print(tree.data,end=' ')
    preOrderTraversal(tree.left)
    preOrderTraversal(tree.right)

def levelTraversal(tree):
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