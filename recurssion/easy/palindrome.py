
count = 0
def count_zero(n):
    global count
    if n == 0: return
    if n % 10 == 0:
        count+=1
    count_zero(n//10)

def count_zeroo(n):
    return helper(n, 0)

def helper(n, c):
    if n == 0: return c

    if n % 10 == 0:
        return helper(n//10, c+1)
    return helper(n//10, c)



print(count_zeroo(7004020000))
print(count)