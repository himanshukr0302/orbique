# 2. WAP to create a list dynamically of n elemnts.

def create_list(n):
    lst = []
    for i in range(n):
        a = input(f"Enter element {i+1}: ")
        lst.append(a)
    print(lst)

if __name__ == '__main__':
    # example: create a list of 5 elements
    create_list(5)
