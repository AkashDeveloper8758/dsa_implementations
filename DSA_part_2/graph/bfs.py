from collections import deque
from implementation import Graph
# breadth first search like level order traversal in tree with unique traversal
def bfs(adj,source,visited:list[bool]):
    q = deque()
    q.append(source)
    visited[source] = True
    while len(q) != 0:
        val = q.popleft()
        print(val,end=' ')
        for v in adj[val]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

def bfsDir(adj,vertices):
    visited = [False for _ in range(vertices)]
    count = 0
    for i in range(vertices):
        if not visited[i]:
            count+=1
            bfs(adj,i,visited)
    print('count is : ',count)


graph = Graph()
v = 7
adj = [[] for _ in range(v)]
graph.addEdge(adj,0,1)
graph.addEdge(adj,0,2)
graph.addEdge(adj,1,2)
graph.addEdge(adj,1,3)
graph.addEdge(adj,4,5)
graph.addEdge(adj,5,6)
graph.printGraph(adj)
print('--------------')
bfsDir(adj,v)