class BinaryIndexedTree:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.parent = [0 for _ in range(len(arr)+1)]
    
    def getSum(self,i):
        res = 0
        # incrementing the i as we are starting from 1 for ease of implementation
        i = i+1
        while i> 0:
            res += self.parent[i]
            # this operation will turn the last bit to find the parent
            i = i - i&(-i)
        return res
    
    def updateIndex(self,i,value):
        diff = value - self.arr[i]
        self.arr[i] = value
        i +=1
        n = len(self.arr)-1
        while i <= n:
            self.parent[i] += diff
            # get the next child to update
            i = i + i&(-i)
        