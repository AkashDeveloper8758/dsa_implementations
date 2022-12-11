class Trie:
    def __init__(self):
        self.isEnd = False
        self.chars = [None for _ in range(26)]

def addItemInTrie(root:Trie,key):
    curr = root
    for c in key:
        ind = ord(c) - ord('a')
        if curr.chars[ind] == None:
            curr.chars[ind] = Trie()
        curr= curr.chars[ind]
    curr.isEnd = True

def searchItemInTrie(root:Trie,key):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        if curr.chars[index] == None:
            return False
        curr = curr.chars[index]
    return curr.isEnd

def isTrieEmpty(root:Trie):
    for i in range(26):
        if root.chars[i] != None:
            return False
    return True

def deleteTrie(root:Trie,key,i):
    if root == None:
        return root
    if i == len(key):
        root.isEnd = False
        if isTrieEmpty(root):
            root = None
        return root
    index = ord(key[i])-ord('a')
    if root.chars[index] == None:
        print('key not found')
        return root
    value = deleteTrie(root.chars[index],key,i+1)

    root.chars[index] = value
    if isTrieEmpty(root) and root.isEnd == False:
        root = None
    return root


root = Trie()
addItemInTrie(root,'akash')
addItemInTrie(root,'ankit')
addItemInTrie(root,'aka')
addItemInTrie(root,'walton')
print('searching : ',searchItemInTrie(root,'aka'))
root = deleteTrie(root,'akash',0)
print('searching after delete: ',searchItemInTrie(root,'aka'))
