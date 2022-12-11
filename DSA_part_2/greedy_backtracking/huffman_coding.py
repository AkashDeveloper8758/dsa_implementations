import heapq

class HuffmanItem:
    def __init__(self,character,freq):
        self.character = character
        self.freq = freq

class Node:
    def __init__(self,data:HuffmanItem,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self,other):
        return self.data.freq < other.data.freq
    
# ---------------- main code ----------------------
def buildHuffmanTree(huffmanList:list[HuffmanItem]):
    myheap:list[Node] = []
    for i in huffmanList:
        node = Node(data=i)
        heapq.heappush(myheap,node)
    # building a BST like structure for ease of search
    while len(myheap) > 1:
        a = heapq.heappop(myheap)
        b = heapq.heappop(myheap)
        newNode = Node(data=HuffmanItem('$',a.data.freq + b.data.freq))
        newNode.left = a
        newNode.right = b
        heapq.heappush(myheap,newNode)
    return myheap[0]

def printCodes(root:Node,s):
    if root == None:
        return
    if root.data.character != '$':
        print(root.data.character,' '+s)
        return
    printCodes(root.left,s+'0')
    printCodes(root.right,s+'1')



huffmanList = [HuffmanItem('a',30),HuffmanItem('d',40),HuffmanItem('e',80),HuffmanItem('f',60)]
root = buildHuffmanTree(huffmanList)
printCodes(root,'')



