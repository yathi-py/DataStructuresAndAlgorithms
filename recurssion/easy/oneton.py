
def oneton(n):

    if n==0:
        return
    oneton(n-1)
    print(n)

oneton(1)