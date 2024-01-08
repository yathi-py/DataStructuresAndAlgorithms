# Number of steps to reduce a number to zero


def reduce_to_zero(n):
    return helper(n,0)

def helper(n, steps):
    if n == 0: return steps

    if n % 2 == 0:
        return helper(n//2, steps+1)
    return helper(n-1, steps+1)

print(reduce_to_zero(14))