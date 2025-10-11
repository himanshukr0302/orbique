# 3.Write a python program to generate fibonacci Series.

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def main():
    try:
        n = int(input("Enter how many Fibonacci terms to generate: ").strip())
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    series = fibonacci(n)
    print("Fibonacci series:")
    print(', '.join(map(str, series)))

if __name__ == "__main__":
    main()
