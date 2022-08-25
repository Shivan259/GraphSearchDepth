def dfs(vertex, G, used):
    global badbriges
    used.add(vertex)
    for neighbour in G[vertex]:
        if colors[vertex] != colors[neighbour]:
            badbriges += 1
        if neighbour not in used:
            dfs(neighbour, G, used)


N = int(input())
G = {}
for i in range(N):
    a = list(input().split())
    bridges = set()
    for j in range(N):
        if a[j] == '1':
            bridges.add(j)
    G[i] = bridges
input()
colors = input().split()
colors = list(map(int, colors))
badbriges = 0
used = set()
for vertex in G:
    if vertex not  in used:
        dfs (vertex, G, used)
print(badbriges // 2)
