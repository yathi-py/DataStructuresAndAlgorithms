


def pattern(r,c):
    if r ==0:
        return

    if c < r:
        pattern(r, c+1)
        print('*', end='')

    else:
        pattern(r-1, 0)
        print('\n')


pattern(5,0)