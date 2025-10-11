# 7.exchange two numbers value without using third number

def swap_arithmetic(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


def swap_pythonic(a, b):
    # the preferred Python way
    return b, a


def main():
    try:
        a = float(input("Enter first number (a): ").strip())
        b = float(input("Enter second number (b): ").strip())
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    print(f"Before swapping: a = {a}, b = {b}")
    a1, b1 = swap_arithmetic(a, b)
    print(f"After arithmetic swap: a = {a1}, b = {b1}")
    a2, b2 = swap_pythonic(a, b)
    print(f"After pythonic swap: a = {a2}, b = {b2}")

if __name__ == "__main__":
    main()
