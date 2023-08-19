n = int(input())
x = int(0)
y = int(0)
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
ls = [0] * n
for i in l1:
    ls[x] = l1[x] + l2[x]
    x = x + 1
for i in ls:
    print(ls[y], end = ' ')
    y = y + 1