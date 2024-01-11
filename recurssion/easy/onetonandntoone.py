

def onetonandntoone(n):

    if n == 0:
        return

    print(n)
    onetonandntoone(n-1)
    print(n)

onetonandntoone(10)