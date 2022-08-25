def dfs(vertex, G, used2):
    global b
    used2.add(vertex)
    for neighbour in G[vertex]:
        if neighbour in used2:
            cycle.append(neighbour)
            cycle.append(vertex)
            return False
        else:
            a = dfs(neighbour, G, used2)
            if b:
                if not a:
                    if vertex not in cycle:
                        cycle.append(vertex)
                        return False
                    else:
                        b = False
                        return False
            else:
                return False
    return True


N, M = [int(x) for x in input().split()]
G = {}
for i in range(N):
    G[i] = set()
for i in range(M):
    u, v = [int(x) for x in input().split()]
    if (u >= N) or (v >= N):
        print('Vertex out of graph')
        exit()
    G[u].add(v)
cycle = []
used = set()
a = True
b = True
for vertex in G:
    if vertex not in used and a:
        used2 = set()
        a = dfs(vertex, G, used2)
        used.union(used2)
if a:
    print('YES')
else:
    cycle.reverse()
    for i in range(len(cycle)):
        print(cycle[i], end=' ')