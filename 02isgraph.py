n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    s = input()
    a[i] = s.split()
    a[i] = list(map(int, a[i]))
IsGraph = True
for i in range(n):
    for j in range (n):
        if a[i][j] not in {0, 1}:
            IsGraph = False
        if i == j:
            if a[i][j] != 0:
                IsGraph = False
        else:
            if a[i][j] != a[j][i]:
                IsGraph = False
if IsGraph:
    print('YES')
else:
    print('NO')
