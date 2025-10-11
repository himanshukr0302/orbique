# 6.create a list dynamically (user input ) with five elements?

# Create a list of five elements using user input

def main():
    lst = []
    for i in range(5):
        val = input(f"Enter element {i+1}: ")
        lst.append(val)
    print('List created:', lst)

if __name__ == '__main__':
    main()
