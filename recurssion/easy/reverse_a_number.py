import math

sum = 0
def reverse_a_number(n):
    global sum
    if not n :
        return
    leng = int(math.log10(n))
    d = n %10
    sum = sum + (d*10**leng)
    reverse_a_number(n//10)

reverse_a_number(198700)
print(sum)


def rev(n):
    return helper(n, 0)

def helper(n, sum):
    if n == 0: return sum
    leng = int(math.log10(n))
    rem = n % 10
    sum = sum + (rem * (10 **leng))
    return helper(n//10, sum)

print(rev(20345))