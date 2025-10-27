'''
11.how to convert  a heterogenous data to homogenous data give an example ?
   (hint convert a list to an array)
'''

import array

lst = [1, "2", 3.0, 4]         
int_arr = array.array('i', map(int, lst))

lst = int_arr.tolist()
print(lst)
