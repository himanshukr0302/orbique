# 4.implement recursion using a function

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    try:
        n = int(input("Enter a non-negative integer to compute its factorial: ").strip())
        if n < 0:
            print("Please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print(f"Factorial of {n} is {factorial(n)}")

if __name__ == "__main__":
    main()
