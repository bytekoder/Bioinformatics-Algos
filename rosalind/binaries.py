def perms(n):
    if not n:
        return

    for i in xrange(2 ** n):
        s = bin(i)[2:]
        s = "0" * (n - len(s)) + s
        yield s

print list(perms(3))
