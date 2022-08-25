N, M = [int(x) for x in input().split()]
a = []
b = []
for i in range(M):
    u, v = [int(x) for x in input().split()]
    a.append(u)
    b.append(v)
CanDivide = True
for i in range(len(a)):
    if a[i] in b:
        CanDivide = False
if CanDivide:
    for i in range(len(b)):
        print(b[i], end=' ')
else:
    print('NO')