# q2 print fib series up to n terms
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b