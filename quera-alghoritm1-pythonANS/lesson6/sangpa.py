def vorodi():
    n = int(input())
    w = []
    for i in range(n):
        x = int(input())
        w.append(x)
    return w
w = vorodi()

def prime_checker(x):
    a = int(x ** 0.5)
    j = 1
    for i in range(2, a + 1):
        if x % i == 0:
            j = 0
            break
    return j
def smaller_primes(x):
    primelist = []
    for i in range(2, x):
        if prime_checker(i) == 1:
            primelist.append(i)
    return len(primelist)

def prime_divisor(x):
    primedivisorlist = []
    for i in range(2, x):
        if x % i == 0 and prime_checker(i) == 1:
            o = x // i
            primedivisorlist.append(o)
    return len(primedivisorlist)
def price_calc():
    eachprice = []
    allprice = 0
    for i in w:
        if prime_checker(i) == 1:
            eachprice.append(int(smaller_primes(i)))
        else:
            eachprice.append(int(prime_divisor(i)))

    for i in eachprice:
        allprice += int(i)

    return allprice
allprice = price_calc()

def discount():
    if prime_checker(allprice) == 1:
        takhfif = smaller_primes(allprice)
    else:
        takhfif = prime_divisor(allprice)
    return takhfif


print(allprice - discount())
