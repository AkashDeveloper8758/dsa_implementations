from collections import deque
from implementation import Graph

# searching from depth first
def dfs(adj,visited:list[bool],s):
    visited[s] = True
    print(s,end=' ')
    for i in adj[s]:
        if not visited[i]:
            dfs(adj,visited,i)

def dfsDis(adj,v):
    visited = [False for _ in range(v)]
    for i in range(v):
        if not visited[i]:
            dfs(adj,visited,i)



graph = Graph()
v = 7
adj = [[] for _ in range(v)]
graph.addEdge(adj,0,1)
graph.addEdge(adj,0,2)
graph.addEdge(adj,1,2)
graph.addEdge(adj,1,3)
graph.addEdge(adj,4,5)
graph.addEdge(adj,5,6)
# graph.printGraph(adj)
dfsDis(adj,v)