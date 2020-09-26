def recursion(n):
    print(int(n), end=' ')
    if n == 1:
        pass
    elif n % 2 == 0:
        recursion(n/2)
    else:
        recursion( 3*n + 1 )

recursion(27)
print(' ')