# use tree data structure to store the parent of multiple nodes
# same parent defines the union logic
class DisjointSet:
    def __init__(self,n) -> None:
        self.parent = [i for i in range(n)]
        # rank is used to reduce the height of tree up to 1.
        # higher ranker will become parent
        self.rank = [0 for _ in range(n)]

    def find(self,x):
        if self.parent[x] == x:
            return x
        # path compression, if the chain is long from parent to child, it makes the child 
        # the direct child of the parent thus compress the total path
        # it reduce the height of the tree up to 1 only.
        self.parent[x] = self.find(self.parent[x])
        return self.find(self.parent[x])

    def union(self,x,y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return
        if self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        elif self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        else:
            self.parent[yp] = xp
            self.rank[xp]+=1



    

