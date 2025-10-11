# 4.create a class with all access specifiers (private,protected,public)
#   then assign some values to data members and by using a display() function
#   print their values.

class Demo:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

    def display(self):
        print('public:', self.public)
        print('protected:', self._protected)
        # access private using name mangling
        print('private:', self._Demo__private)

if __name__ == '__main__':
    d = Demo()
    d.display()
