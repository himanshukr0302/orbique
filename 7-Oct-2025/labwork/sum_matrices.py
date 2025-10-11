# 6. WAP to find sum of two matrix and place in third matrix.

def sum_of_two_matrix(matrix1, matrix2):
    sum_matrix = []
    for i in range(len(matrix1)):
        sum_matrix.append([])
        for j in range(len(matrix1[0])):
            sum_matrix[i].append(matrix1[i][j] + matrix2[i][j])
    return sum_matrix

if __name__ == '__main__':
    matrix1 = [[1,2],[3,4]]
    matrix2 = [[5,6],[7,8]]
    print(sum_of_two_matrix(matrix1, matrix2))
