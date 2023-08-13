maghsomelaih = int(input())
def num_divs(k):
    y1 = 0
    for i in range(1000):
        y1 = y1 + i
        b = 0
        for j in range(1, y1 + 1):
            if y1 % j == 0:
                b = b + 1
        if b >= maghsomelaih:
            break
    return y1
print(num_divs(maghsomelaih))