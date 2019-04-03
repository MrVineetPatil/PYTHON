def bfs(v):
    visited[v]=1
    L=[v]
    while len(L)!=0:
        v=deleteq(L)
        for j in range (1,n+1):
            if ([v,j] in edgelist or [j,v] in edgelist) and visited[j]!=1:
                print(j)
                visited[j]=1
                L.append(j)
edgelist=[]
visited=[]

def deleteq(L):
    item=L[0]
    L.remove(item)
    return item

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
bfs(j)