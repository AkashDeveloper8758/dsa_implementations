import math

from implementation import Graph


class DisjointSet:
    def __init__(self,n) -> None:
        self.parent = [i for i in range(n)]
        # rank is used to reduce the height of tree.
        # higher ranker will become parent
        self.rank = [0 for _ in range(n)]

    def find(self,x):
        if self.parent[x] == x:
            return x
        # path compression, if the chain is long from parent to child, it makes the child 
        # the direct child of the parent thus compress the total path
        # it reduce the height of the tree
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
    


def dfsTopological(adj,st,visited,s):
    visited[s] = True
    for u in adj[s]:
        if not visited[u]:
            dfsTopological(adj,st,visited,u)
    st.append(s)

# using topological sort
def shortestPathInWeightedGraph(adj,v,weight,s=0):
    visited = [False for _ in range(v)]
    stack = []
    for i in range(v):
        if not visited[i]:
            dfsTopological(adj,stack,visited,i)
    dist = [math.inf for _ in range(v)]
    
    # reverse stack so top of the graph come in the beginning instead of last
    stack.reverse()
    print('stack: ',stack)
    dist[s] = 0
    for u in stack:
        for v in adj[u]:
            if dist[v] > dist[u] + weight[u][v]:
                dist[v] = dist[u] + weight[u][v]
    print('distances : ',dist)

def primsAlgorithm(weights,adj,v):
    visited = [False for _ in range(v)] #to store vertices which are in minimum set now
    dist = [math.inf for _ in range(v)] # used to store the weights of vertices
    
    parent = [-1 for _ in range(v)] # to store the parent to which it is reachable with min weight
    dist[0] = 0 # root vertex weight is always 0
    res = 0 # mst value
    for _ in range(v):
        minv = -1
        # find min dist to add to the visited
        for j in range(v):
            if not visited[j] and ( minv == -1 or dist[minv] > dist[j] ):
                minv = j
        visited[minv] = True
        print('minv = ',dist[minv])
        res += dist[minv]
        for u in adj[minv]:
            if not visited[u] and weight[u][minv] != 0 and weights[u][minv] < dist[u]:
                dist[u] = weights[u][minv]
                parent[u] = minv
    print('total min weight : ',res)
    print('parentset : ',parent)

def dikstraAlgorithm(graph:list[list],s=0):
    v = len(graph)
    visited = [False for _ in range(v)]
    dist = [math.inf for _ in range(v)]
    dist[s]= 0

    for _ in range(v):
        u = -1
        for i in range(v):
            if not visited[i] and (u == -1 or dist[u] > dist[i] ):
                u = i
        visited[u]= True
        for i in range(v):
            if not visited[i] and graph[u][i] != 0:
                dist[i] = min(dist[i],dist[u]+graph[u][i])

    return dist

# bellmen ford sortest path with neg cycle detection
# after v-1 iteration for every edge every edge will be sorted
# and if not then there is a neg cycle present in the graph
def bellmanFordAlgo(weights,vertices):
    dist = [math.inf for _ in range(vertices)]
    dist[0] = 0
    for _ in range(vertices-1):
        for u,v,w in weights:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
    for u,v,w in weights:
        if dist[u] > dist[v]+w:
            print('neg cycles present')
    print('dist :',dist)

# Floyd Warshall
def floydWarshellShortestDistance(matrix):
    v = len(matrix)
    INF = 1<<32
    for i in range(v):
        for j in range(v):
            if matrix[i][j] == -1:
                matrix[i][j] = INF
    # trying all vertices
    for k in range(v):
        # selecting sourcd
        for i in range(v):
            # selecting destination
            for j in range(v):
                if matrix[i][k] < INF and matrix[k][j] < INF and matrix[i][k] + matrix[k][j] < INF:
                    matrix[i][j] = min(matrix[i][j],matrix[i][k] + matrix[k][j])
    for i in range(v):
        for j in range(v):
            if matrix[i][j] == INF:
                matrix[i][j] = -1 

# bigO = eloge
def krushkalAlgo(graph:list[list],v):
    # ---- disjoint set implementation ----- 
    dset = DisjointSet(v)
    graph.sort(key=lambda item: item[2])
    mst = []
    res = 0
    s,i=0,0
    # until the size bofore vertices - 1
    while s < v-1:
        item = graph[i]
        x = dset.find(item[0])
        y = dset.find(item[1])
        if x != y:
            mst.append(item)
            dset.union(x,y)
            res+= item[2]
            s+=1
        i+=1
    print(mst)
    return res


graph = Graph()
weight = [
[0,2,0,0,1,0],
[2,0,3,0,0,0],
[0,3,0,6,0,0],
[0,0,6,0,0,1],
[1,0,2,0,0,4],
[0,0,0,1,4,0]
]
weightList = [
    [0,1,1],
    [0,4,2],
    [1,2,1],
    [2,3,4],
    [3,5,2],
]
v = 6
adj = [[] for _ in range(v)]
graph.addDirectedEdge(adj,0,1)
graph.addDirectedEdge(adj,0,4)
graph.addDirectedEdge(adj,1,2)
graph.addDirectedEdge(adj,4,2)
graph.addDirectedEdge(adj,4,5)
graph.addDirectedEdge(adj,2,3)
graph.addDirectedEdge(adj,5,3)
# shortestPathInWeightedGraph(adj,v,weight,1)
# primsAlgorithm(weight,adj,v)
# print('shortest paths : ',dikstraAlgorithm(weight))
# bellmanFordAlgo(weightList,v)
print('kruskal res : ',krushkalAlgo(weightList,v))
