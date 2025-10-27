'''
11.how to convert  a heterogenous data to homogenous data give an example ?
   (hint convert a list to an array)
'''
import numpy as np
heterogeneous_list = [1, 2.5, '3', 4, '5.5']
homogeneous_array = np.array(heterogeneous_list, dtype=float)
print("Heterogeneous List:", heterogeneous_list)
print("Homogeneous Array:", homogeneous_array)
