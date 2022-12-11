import sys
sys.setrecursionlimit(10000)

from collections import deque
from DSA_part_2.bst.tree import Tree

def buildTree(s):
    if len(s) == 0 or s[0] == 'N':
        return None
    ip = list(map(str,s.split()))
    root = Tree(int(ip[0]))
    size = 0
    q = deque()
    q.append(root)
    size+=1
    i=1
    while size > 0 and i < len(ip):
        currNode = q[0]
        q.popleft()
        size+=1
        currVal = ip[i]
        if currVal != 'N':
            currNode.left = Tree(int(currVal))
            q.append(currNode.left)
            size+=1
        i+=1
        if i>= len(ip):
            break
        currVal = ip[i]
        if currVal != 'N':
            currNode.right = Tree(int(currVal))
            q.append(currNode.right)
            size+=1
        i+=1
    return root


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
def preOrderTraversal(tree:Tree):
    if tree == None:
        return
    print(tree.data,end=' ')
    preOrderTraversal(tree.left)
    preOrderTraversal(tree.right)
