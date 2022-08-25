def dfs(vertex: int, G, visited, ans):
    global Cycle
    visited[vertex] = True
    gray.add(vertex)
    for neighbour in G[vertex]:
        if neighbour in gray:
            Cycle = True
        if not visited[neighbour]:
            dfs(neighbour, G, visited, ans)
    gray.remove(vertex)
    ans.append(vertex)


N, M = [int(x) for x in input().split()]
G = {}
correct = True
for i in range(N):
    G[i] = set()
for i in range(M):
    u, v = [int(x) for x in input().split()]
    if (u >= N) or (v >= N):
        print('NO')
        exit()
    G[u].add(v)
visited = [False]*N
ans = []
Cycle = False
for i in range(N):
    if not visited[i]:
        gray = set()
        dfs(i, G, visited, ans)
ans.reverse()
if not Cycle:
    for i in range(len(ans)):
        print(ans[i], end=' ')
else:
    print('NO')