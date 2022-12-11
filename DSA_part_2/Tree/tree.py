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