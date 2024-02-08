n, m = map(int, input().split())
matrix = []
kcost = 0

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for _ in range(m):
    yk, xk = map(int, input().split())
    kcost += matrix[yk-1][xk-1]

print(kcost)
