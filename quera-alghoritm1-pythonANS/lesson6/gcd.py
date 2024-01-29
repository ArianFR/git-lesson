def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
n = int(input())
my_list = [int(x) for x in range(1, n)]
list2 = []

for i in my_list:
    if gcd(i, n) == 1:
        list2.append(i)
v = lcm(list2[0], list2[1])
for i in list2[2::]:
    v = lcm(i, v)
print(v)