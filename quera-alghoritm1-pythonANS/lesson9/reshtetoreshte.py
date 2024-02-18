string = str(input())
a = str(input())
a1 = len(a)
out = []
for i in range(len(string)+1):
    if string[i:i + a1] == a:
        out.append(str(i+1))
print(' '.join(out))
