#User function Template for python3
class Trie:
    def __init__(self):
        self.isEnd= False
        self.chars = {}
        
class Solution:
    def addToTrie(self,root,word):
        curr = root
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Trie()
            curr = curr.chars[c]
        curr.isEnd = True

    def searchWord(self,root:Trie,word):
        curr =root
        for c in word:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]
        return curr.isEnd

    def searchSplit(self,root:Trie,word):
        n = len(word)
        curr = root
        cut = 0
        i = 0
        iupdate = 0
        while i < n:
            if word[i] in curr.chars:
                curr = curr.chars[word[i]]
                if curr.isEnd:
                    cut = i
                i+=1
            else:
                if cut+1 == iupdate:
                    print('can not find : ',word[i])
                    return False
                i = cut+1
                iupdate = i
                curr = root
        return cut == i-1
    
    def searchSplit2(self,root:Trie,word):
        if len(word) == 0:
            return True
        n = len(word)
        for i in range(1,n+1):
            if self.searchWord(root,word[:i]) and self.searchSplit2(root,word[i:]):
                return True
        return False


            
    def wordBreak(self,strv,arr):
        root = Trie()
        for w in arr:
            self.addToTrie(root,w)
        return self.searchSplit2(root,strv)

        

arr = ['i', 'like', 'sam', 'sung', 'mobile', 'ice', 
  'cream', 'icecream', 'man', 'go', 'mango','crea']

print(Solution().wordBreak("thequickbrownfox",
                           ["the", "quick", "fox", "brown"]))
print(Solution().wordBreak("bedbathandbeyond", [
      "bed", "bath", "bedbath", "and", "beyond"]))
print(Solution().wordBreak("bedbathandbeyond", [
      "teddy", "bath", "bedbath", "and", "beyond"]))

print(Solution().wordBreak("bedbathandaway", [
      "bed", "bath", "bedbath", "and", "away"]))

# print('res : ',Solution().findSplit(arr,'ilikesamsung'))