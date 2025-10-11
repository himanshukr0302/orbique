# 1.print alphabets from a to z

def main():
    for code in range(ord('a'), ord('z') + 1):
        print(chr(code), end=' ')
    print()

if __name__ == '__main__':
    main()
