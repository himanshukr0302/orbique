'''
10.Generate a unit matrix for displaying that 
data points are existing diagonally in the matrix.  
'''
def generate_unit_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

size = 4
unit_matrix = generate_unit_matrix(size)
for row in unit_matrix:
    print(row)