# 2.print the following fibonacci series
#    0,1,1,2,3,5,8,13......

# Print Fibonacci series up to n terms

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=',')
        a, b = b, a + b
    print()

if __name__ == '__main__':
    try:
        n = int(input('Enter number of Fibonacci terms to print: ').strip())
        if n <= 0:
            print('Please enter a positive integer.')
        else:
            fibonacci(n)
    except ValueError:
        print('Invalid input.')
