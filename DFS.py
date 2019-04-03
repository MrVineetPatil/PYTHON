def dfs(v):
    visited[v]=1
    print(v)
    R=[v]
    while len(R)!=0:
        v=R.pop()
        for j in range(1,n+1):
            if ([v,j] in edgelist or [j,v] in edgelist) and visited[j]!=1:
                R.append(j)
                dfs(j)

edgelist=[]
visited=[]
n=int(input("Enter the number of vertices: "))
for i in range (n+1):
    visited.append(0)
print(visited)
edges = int(input("Enter the number of edges: "))
for i in range (edges):
    edgelist.append([])
print ("Input edges ")
for i in range(edges):
    k = list(map(int,input().split(" ")))
edgelist[i] = k
print ("Enter initial vertex ")
j = int(input())
dfs(j)