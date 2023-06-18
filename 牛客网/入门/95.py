def mon(n):
    if n == 1:
        return 2
    if n == 0:
        return 1
    else:
        return mon(n-1) + mon(n-2)

print(mon(int(input())))