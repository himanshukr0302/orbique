# 10.check your input is phone number and validate it with starting numbers 6,7,8,9

def is_valid_phone(number_str):
    # remove spaces and common separators
    cleaned = ''.join(ch for ch in number_str if ch.isdigit())
    if len(cleaned) != 10:
        return False
    if cleaned[0] not in '6789':
        return False
    return True


def main():
    s = input("Enter a phone number: ").strip()
    if is_valid_phone(s):
        print("Valid phone number.")
    else:
        print("Invalid phone number. It must be 10 digits and start with 6,7,8 or 9.")

if __name__ == "__main__":
    main()
