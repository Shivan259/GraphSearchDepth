n = int(input())
a = []
s = 0
for i in range (n):
    a = input().split()
    for j in  range(n):
        s += int(a[j])
s = s // 2
print(s)