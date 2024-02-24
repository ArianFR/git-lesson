from itertools import permutations


def next_permutation(x):
    x_str = str(x)
    digits = [int(d) for d in x_str]

    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return 0
    j = len(digits) - 1
    while j > i and digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]

    digits[i + 1:] = reversed(digits[i + 1:])

    next_x = int(''.join(map(str, digits)))
    return next_x if next_x > x else -1


x = int(input())
result = next_permutation(x)
print(result)
