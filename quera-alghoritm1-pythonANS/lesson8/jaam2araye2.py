n, m = map(int, input().split())
l1 = []
l2 = []
c = []
for i in range(n):
    lp1 = list(map(int, input().split()))
    l1.append(lp1)

for i in range(n):
    lp2 = list(map(int, input().split()))
    l2.append(lp2)

for i in range(n):
    for j in range(m):
        w = str(l1[i][j] + l2[i][j])
        c.append(w)
    e = ' '.join(c)
    print(e)
    c = []
