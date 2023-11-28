def swoprow(matrix, row1, row2):
    temp_matrix = []
    for i in range(len(matrix)):
        temp_matrix.append(matrix[i])
    temp_matrix[row1], temp_matrix[row2] = temp_matrix[row2], temp_matrix[row1]
    return temp_matrix

if __name__ == '__main__':
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [-1, -2, -3, -4]]
    print(A)
    print('After swop')
    Ap = swoprow(A, 0, 3)
    print('A=', A)
    print("A'=", Ap)