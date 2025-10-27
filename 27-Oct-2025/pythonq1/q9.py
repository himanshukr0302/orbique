'''
9.Write a python program to display a variable value,type and id ?
'''
def display_variable_info(var):
    print(f"Value: {var}")
    print(f"Type: {type(var)}")
    print(f"ID: {id(var)}")

# Example usage
my_variable = 42
display_variable_info(my_variable)