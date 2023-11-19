def read_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix

def add_mat(file_name1, file_name2, result_file_name):
    matrix1 = read_matrix(file_name1)
    matrix2 = read_matrix(file_name2)

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        with open(result_file_name, 'w') as result_file:
            result_file.write('')
        return

    result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    with open(result_file_name, 'w') as result_file:
        for row in result_matrix:
            result_file.write(' '.join(map(str, row)) + '\n')

add_mat('mat1.txt', 'mat2.txt', 'outmat.txt')
add_mat('mat1.txt', 'mat3.txt', 'outmat1.txt')