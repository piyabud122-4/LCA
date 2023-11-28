def read_matrix(file_name):

    with open(file_name, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file.readlines()]
    return matrix

def write_matrix(file_name, matrix):

    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def add_mat(file_name1, file_name2, result_file_name):

    matrix1 = read_matrix(file_name1)
    matrix2 = read_matrix(file_name2)
    matrix3 = read_matrix(file_name2)

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        open(result_file_name, 'w').close()
    else:
        result_matrix = [[matrix1 + matrix2 ]]
        write_matrix(result_file_name, result_matrix)

    if len(matrix1) != len(matrix3) or len(matrix1[0]) != len(matrix3[0]):
        open(result_file_name, 'w').close()
    else:
        result_matrix = [[matrix1[i][j] + matrix3[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        write_matrix(result_file_name, result_matrix)

add_mat('mat1.txt', 'mat2.txt', 'outmat.txt')
add_mat('mat1.txt', 'mat3.txt', 'outmat1.txt')