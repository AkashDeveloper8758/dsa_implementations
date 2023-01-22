from collections import deque
from implementation import Graph

# bfs
def shortestPathToAll(adj,s,v):
    visited = [False for _ in range(v)]
    dist = [-1 for _ in range(v)]

    visited[s] = True
    dist[s] = 0
    q = deque()
    q.append(s)
    while len(q) != 0:
        val = q.popleft()
        visited[val] = True
        for u in adj[val]:
            if not visited[u]:
                visited[u] = True
                dist[u] = dist[val]+1
                q.append(u)
    print(dist)


def dfsRec(adj,s,visited,parent):
    visited[s] = True
    for u in adj[s]:
        print('u : ',u)
        if not visited[u]:
            visited[u] = True
            # current source will become parent for next call
            if dfsRec(adj,u,visited,s):
                return True
        elif u != parent:
            return True
    return False

# using dfs
# undirected graph
def detectCycleInGraph(adj,v):
    visited = [False for _ in range(v)]
    for i in range(v):
        if visited[i] == False:
             if dfsRec(adj,i,visited,-1):
                 return True
    return False
    
# --------- directed graph --------------
# if any decendent has a back edge to any ancester then there is a cycle.

def dfsRec2(adj,visited,recStack,s):
    visited[s] = True
    recStack[s] = True
    for u in adj[s]:
        if not visited[u] and dfsRec2(adj,visited,recStack,u):
            return True
        elif recStack[u]:
            return True
    recStack[s] = False
    return False


def isCycleIndirectedGraph(adj,v):
    visited = [False for _ in range(v)]
    recStack = [False for _ in range(v)]
    for i in range(v):
        if not visited[i]:
            if dfsRec2(adj,visited,recStack,i):
                return True
    return False

#* ------------- topological sort -------------
# topological graph is a special graph in which some nodes have 0 depencencies and other 
# depend on them
# kan's algo
# in cyclic graph
def bfsTopological(adj,indegree,visited):
    q = deque()
    # s has 0 dependencies
    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    count = 0
    while len(q) != 0:
        val = q.popleft()
        count+=1
        visited[val] = True
        # print(val,end=' ')
        for u in adj[val]:
            if not visited[u]:
                if indegree[u] ==0:
                    q.append(u)
                else:
                    indegree[u] -= 1
                    if indegree[u]==0:
                        q.append(u)
    return count


def topologicalSortTraversal(adj,v):
    indegree = [0 for _ in range(v)]
    visited = [False for _ in range(v)]
    for i in adj:
        for j in i:
            indegree[j]+=1
    print(indegree)
    c = bfsTopological(adj,indegree,visited)
    # if there is a cycle, then some of node's indegres will remains more than 0, and will
    # be not couted, and c will always be less then v, in that case.
    if c != v:
        print('cyclic')
    else:
        print('acyclic')

    #* ------------ topological sort using DFS
    #* add the dependent nodes first then add the parent at last

def dfsTopological(adj,st,visited,s):
    visited[s] = True
    for u in adj[s]:
        if not visited[u]:
            dfsTopological(adj,st,visited,u)
    st.append(s)

def topologicalSortUsingDFS(adj,v):
    visited = [False for _ in range(v)]
    stack = []
    for i in range(v):
        if not visited[i]:
            dfsTopological(adj,stack,visited,i)
    while stack:
        print(stack.pop(),end=' ')
    
def greedyGraphColoring(adj,v):
    available = [False for _ in range(v)]
    resc = [-1 for _ in range(v)]
    resc[0] = 0
    for u in range(1,v):
        for i in adj[u]:
            if resc[i] != -1:
                available[resc[i]] = True
        cr = 0
        while cr < v:
            if available[cr] == False:
                break
            cr+=1
        resc[u] = cr
        for i in adj[u]:
            if resc[i] != -1:
                available[resc[i]] = False
    print(resc)


timer = 0
def DFSbridge(s,adj,res,visited,low,dist,parent):
    global timer
    low[s] = dist[s] = timer
    timer+=1
    visited[s] = True
    for c in adj[s]:
        if not visited[c]:
            parent[c] = s
            DFSbridge(c,adj,res,visited,low,dist,parent)

            # compare the low with child, if low found update source low
            low[s] = min(low[s],low[c])
            # if child low is greater then parent distance means, there is no way to reach 
            # child except the parent , so this is a bridge.
            if low[c] > dist[s]:
                res.append([s,c])
        elif c != parent[s]:
            # check if child is not parent, then there is a mininum distance possible from distance of child.
            low[s] = min(low[s],dist[c])

def findBridges(adj,v):
    visited = [False for _ in range(v)]
    res = []
    low = [float('inf') for _ in range(v)] # to store lowest visited value
    dist = [float('inf') for _ in range(v)] # distance in recursion call
    parent = [-1 for _ in range(v)] # to store parent because we cant take dist value of parent

    for i in range(v):
        if not visited[i]:
            DFSbridge(i,adj,res,visited,low,dist,parent)
    return res

# jug1 of 'a' capacity, jug2 of 'b' capacity , check if target is possible
def jugProblem(a,b,target):
    q = deque()
    path = []
    visited = {}
    # initially both of jug are empty
    q.append([0,0])
    while q:
        val = q.popleft()
        # if we have visited same cobination before
        if (val[0],val[1]) in visited:
            continue
        if val[0] > a or val[1] > b or val[0] < 0 or val[1] < 0:
            continue

        path.append([val[0],val[1]])
        visited[(val[0],val[1])] = True
        if val[0] == target or val[1] == target:
            if val[0] == target:
                path.append([val[0],0])
            else:
                path.append([0,val[1]])
            return path
        
        # fill jug1 keeping jug2
        q.append([a,val[1]])

        # fill jug2 keeping jug1
        q.append([val[0],b])
        
        # trying every possible transfer from 0 to max(a,b)
        for ab in range(max(a,b)+1):
            # from jug1 to jug 2:
            c = val[0] - ab
            d = val[1] + ab
            if d == b or c >=0:
                q.append([c,d])
            
            # from jug2 to jug1
            c = val[0] + ab
            d = val[1] - ab
            if c == a or d >=0:
                q.append([c,d])
        
        # empty jug1 and fill jug2
        q.append([0,b])
        q.append([a,0])
    print('not solvable !')
    return []





graph = Graph()
v = 7
adj = [[] for _ in range(v)]
graph.addEdge(adj,0,1)
graph.addEdge(adj,0,2)
graph.addEdge(adj,1,2)
graph.addEdge(adj,2,3)
graph.addEdge(adj,3,4)
# graph.addEdge(adj,1,5)
graph.addEdge(adj,5,3)
# shortestPathToAll(adj,0,v)
# topologicalSortTraversal(adj,v)
# topologicalSortUsingDFS(adj,v)

# newadj = [[], [2], [1, 3], [2]]
# print('detect cycle : ',detectCycleInGraph(newadj,4))
# greedyGraphColoring(adj,v)
# print('bridges : ',findBridges(adj,v))

print('jug path : ',jugProblem(4,3,2))




