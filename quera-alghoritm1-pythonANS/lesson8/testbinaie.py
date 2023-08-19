n = int(input())
x = str(input())
y = str(input())
xl = []
yl = []
g = int(0)
def strtolist(a, b):
    for i in a:
        xl.append(i)
    for i in b:
        yl.append(i)
    return xl, yl
strtolist(x, y)
for i in range(len(xl)):
    if xl[i] != yl[i]:
        g = g + 1
print(g)