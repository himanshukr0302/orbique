'''
6.create a list dynamically (user input ) with five elements?
'''
n = int(input("Enter number of elements you want in the list: "))
dynamic_list = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    dynamic_list.append(element)
print("The dynamically created list is:", dynamic_list)