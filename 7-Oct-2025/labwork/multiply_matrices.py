# 7. WAP to find multiplication of two matrix and place in third matrix.

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Matrix multiplication is not possible."
    # Initialize the result matrix with zeros
    mul_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                mul_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return mul_matrix

if __name__ == '__main__':
    matrix1 = [[1,2],[3,4]]
    matrix2 = [[5,6],[7,8]]
    print(multiply_matrices(matrix1, matrix2))
