x, y, maxx = map(int, input().split())
mx = []
my = []
for i in range(1, x+1):
    if x % i == 0:
        mx.append(i)
for j in range(1, y+1):
    if y % j == 0:
        my.append(j)
counter = 0
for i in mx:
    for j in my:
        if i + j <= maxx:
            counter = counter + 1
print(counter)