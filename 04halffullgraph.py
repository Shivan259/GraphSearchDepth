N, M = [int(x) for x in input().split()]
G = {}
for i in range(N):
    G[i] = set()
for i in range(M):
    v1,v2 = [int(x) for x in input().split()]
    for u, v in (v1, v2), (v2, v1):
        G[u].add(v)
IsHalfFull = True
for i in range(N):
    if len(G[i]) < N - 1:
        IsHalfFull = False
if IsHalfFull:
    print('YES')
else:
    print('NO')