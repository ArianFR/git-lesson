n, x, y = map(int, input().split())

max_i = n // x
max_j = n // y

for i in range(max_i + 1):
    j = (n - i * x) // y
    if i * x + j * y == n:
        print(i, j)
        exit()

print('-1')
