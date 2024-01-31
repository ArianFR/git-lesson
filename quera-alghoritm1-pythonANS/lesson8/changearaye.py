q = int(input())
ans = []
while q > 0:
    q -= 1
    x = list(map(str, input().split()))
    if x[1] == 'len+1':
        i = int(len(ans)+1)
    else:
        i = int(x[1])-1
    if x[0] == '+':
        ans.insert(i, x[2])
    elif x[0] == '-':
        ans.pop(i)
    if len(ans) == 0:
        print('EMPTY')
    else:
        print(' '.join(ans))

