# 9.assume your ai has been given a number ask it to display its cube root...validate the given number whole number output.

def is_perfect_cube(n):
    if n < 0:
        root = round(abs(n) ** (1/3))
        return -root, ( -root) ** 3 == n
    root = round(n ** (1/3))
    return root, root ** 3 == n


def main():
    try:
        n = int(input("Enter an integer to find its cube root: ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    root, is_perfect = is_perfect_cube(n)
    if is_perfect:
        print(f"The cube root of {n} is {root} (whole number).")
    else:
        print(f"{n} does not have an integer cube root. Approximate cube root: {n ** (1/3):.6f}")

if __name__ == "__main__":
    main()
