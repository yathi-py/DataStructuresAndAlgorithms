

summ = 0

def reverse_a_digit(n):
    global summ
    if n==0:
        return
    rem = n % 10

    summ = summ * 10+rem
    reverse_a_digit(n//10)

reverse_a_digit(1345)
print(summ)
