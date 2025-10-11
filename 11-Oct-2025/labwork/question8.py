# 8.Assume your AI chatbot has been given the following numbers :
#    1,2,3,3,4,4,5,5,5,6,7,8,9,10,11....
# ask him to say one number only one time

def unique_numbers(seq):
    seen = set()
    unique = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            unique.append(x)
    return unique


def main():
    # example list from the problem statement
    nums = [1,2,3,3,4,4,5,5,5,6,7,8,9,10,11]
    print("Original numbers:", nums)
    uniq = unique_numbers(nums)
    print("Numbers with duplicates removed (appear once):")
    print(uniq)

if __name__ == "__main__":
    main()
