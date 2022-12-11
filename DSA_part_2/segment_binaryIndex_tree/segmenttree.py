class SegmentTree:
    def __init__(self,n,arr):
        self.arr = arr
        self.tree = [None for _ in range(4*n)]
    
    def createSegmentTree(self,s,e,si):
        if s==e:
            self.tree[si] = self.arr[s]
            return self.tree[si]
        mid = (s+e)//2
        self.tree[si] = self.createSegmentTree(s,mid,2*si+1) + self.createSegmentTree(mid+1,e,2*si+2)
        return self.tree[si]
    
    def getSum(self,qs,qe,ss,se,i):
        # if query is outside the range
        if qs > se or qe < ss:
            return 0
        # if range is inside the query
        if qs <= ss and qe >= se:
            return self.tree[i]
        
        mid = (ss+se)//2
        return self.getSum(qs,qe,ss,mid,2*i+1) + self.getSum(qs,qe,mid+1,se,2*i+2)
    
    def __updateNodeRec(self,ss,se,si,i,diff):
        # if outside the current range
        if i <= ss or i >= se:
            return
        self.tree[si] = self.tree[si]+diff
        if se > ss:
            mid = (se+ss)//2
            self.__updateNodeRec(ss,mid,2*si+1,i,diff)
            self.__updateNodeRec(mid+1,se,2*si+2,i,diff)

    def updateNode(self,value,i):
        diff  = value-self.arr[i]
        self.__updateNodeRec(0,len(self.arr),0,i,diff)

    

arr = [3,6,1,8,3,9]
st = SegmentTree(len(arr),arr)

st.createSegmentTree(0,len(arr)-1,0)
print(st.tree)
st.updateNode(6,2)
print('after update ',st.tree)
print('get sum : ',st.getSum(0,2,0,len(arr)-1,0))

