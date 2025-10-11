# 5. How to create a unit matrix in python.

def unit_matrix(n):
    unit = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        unit[i][i] = 1
    return unit

if __name__ == '__main__':
    print(unit_matrix(5))
