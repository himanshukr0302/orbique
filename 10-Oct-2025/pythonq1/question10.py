# 10.Generate a unit matrix for displaying that data points are existing diagonally in the matrix.

# Generate an n x n identity (unit) matrix

def unit_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix

if __name__ == '__main__':
    try:
        n = int(input('Enter size n for unit matrix: ').strip())
        print(unit_matrix(n))
    except ValueError:
        print('Invalid input')
