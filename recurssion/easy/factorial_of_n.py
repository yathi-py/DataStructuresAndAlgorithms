
def factorial(n):

    if n < 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))


def sumof(n):
    if n == 1:
        return 1
    return n + sumof(n-1)

print(sumof(5))