import math

def prime_num(a, b):
    for i in range(a, b + 1):
        is_prime = True
        
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            if i != 1:
                print(i)

num1 = int(input())
num2 = int(input())
prime_num(num1, num2)
