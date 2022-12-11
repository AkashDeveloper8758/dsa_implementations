class DisjointSet2:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self,v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.find(self.parent[v])
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] +=1

def krushkalAlgo(graph:list[list],v):
    graph.sort(key=lambda x: x[2])
    dsj = DisjointSet2(v)
    i,s = 0,0
    res = []
    while s < v-1:
        item = graph[i]
        px = dsj.find(item[0])
        py = dsj.find(item[1])
        if px != py:
            res.append(item)
            s+=1
            dsj.union(px,py)
        i+=1
    totalCost = 0
    for u,x,w in res:
        totalCost += w
        print('from : ',[u,x])
    print('total cost : ',w)

weightList = [
    [0,1,1],
    [0,4,2],
    [1,2,1],
    [2,3,4],
    [3,5,2],
]
v = 6
krushkalAlgo(weightList,v)

        