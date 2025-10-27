'''4.create a class with all access specifiers (private,protected,public)
  then assign some values to data members and by using a display() function
  print their values.
'''
class AccessSpecifiers:
    def __init__(self, public_value, protected_value, private_value):
        self.public_var = public_value
        self._protected_var = protected_value
        self.__private_var = private_value

    def display(self):
        print(f"Public Variable: {self.public_var}")
        print(f"Protected Variable: {self._protected_var}")
        print(f"Private Variable: {self.__private_var}")

ob = AccessSpecifiers("I am Public", "I am Protected", "I am Private")
ob.display()