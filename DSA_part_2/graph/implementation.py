class Graph:
    def __init__(self) -> None:
        pass
    def addEdge(self,adj:list[list],v,u):
        adj[v].append(u)
        adj[u].append(v)
    def addDirectedEdge(self,adj:list[list],v,u):
        adj[v].append(u)
    def printGraph(self,adj):
        for i in range(len(adj)):
            for j in adj[i]:
                print(j,end=' ')
            print('')
    