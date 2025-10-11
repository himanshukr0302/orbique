# 5.generate following series up to n number:
# 1+1/2 + 2/3 + 3/4 +4/5 + 5/6+.............
# find sum of the series.

def series_sum(n):
    total = 0.0
    for i in range(1, n+1):
        total += i / (i + 1)
    return total


def main():
    try:
        n = int(input("Enter the number of terms (n): ").strip())
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    total = series_sum(n)
    print(f"Sum of the series up to {n} terms is: {total}")

if __name__ == "__main__":
    main()
