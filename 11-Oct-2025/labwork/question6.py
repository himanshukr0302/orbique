# 6.printing alphabets in Small letters from A-Z and convert them small letters in the same program

def main():
    # generate uppercase A-Z using chr and range
    uppercase = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
    print("Uppercase A-Z:")
    print(' '.join(uppercase))

    # convert to lowercase
    lowercase = [ch.lower() for ch in uppercase]
    print("\nConverted to lowercase a-z:")
    print(' '.join(lowercase))

if __name__ == "__main__":
    main()
