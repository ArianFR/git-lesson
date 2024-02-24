def search_horizontal(table, s):
    count = 0
    for row in table:
        for i in range(len(row) - len(s) + 1):
            if row[i:i+len(s)] == s:
                count += 1
    return count

def search_vertical(table, s):
    count = 0
    for j in range(len(table[0])):
        for i in range(len(table) - len(s) + 1):
            found = True
            for k in range(len(s)):
                if table[i+k][j] != s[k]:
                    found = False
                    break
            if found:
                count += 1
    return count

n, m = map(int, input().split())
table = [input() for _ in range(n)]
s = input()

horizontal_count = search_horizontal(table, s)
vertical_count = search_vertical(table, s)

print(horizontal_count + vertical_count)
