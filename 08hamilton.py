def dfs(vertex: int, G, visited, ans):
    visited[vertex] = True
    ans.append(vertex)
    for neighbour in G[vertex]:
        if neighbour == 0 and False not in visited:
            for i in range(len(ans)):
                print(ans[i], end=' ')
            exit()
        elif not visited[neighbour]:
            dfs(neighbour, G, visited, ans)
    visited[vertex] = False
    ans.pop()


def inputgraph(G, N, M):
    for i in range(N):
        G[i] = set()
    for i in range(M):
        u, v = [int(x) for x in input().split()]
        if (u >= N) or (v >= N):
            print('NO')
            exit()
        G[u].add(v)
        G[v].add(u)
    return G


N, M = [int(x) for x in input().split()]
G = {}
G = inputgraph(G, N, M)
visited = [False]*N
ans = []
dfs(0, G, visited, ans)
print('NO')