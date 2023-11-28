def gauss_jordan(A,b):
    if len(A) != len(b):
        return None
    augmented_matrix = [row + b_row for row, b_row in zip(A, b)]
    n = len(A)
    for i in range(n):
        pivot = augmented_matrix[i][i]
        for j in range(len(augmented_matrix[i])):
            augmented_matrix[i][j] /= pivot
        for r in range(n):
            if r != i:
                factor = augmented_matrix[r][i]
                for j in range(len(augmented_matrix[r])):
                    augmented_matrix[r][j] -= factor * augmented_matrix[i][j]
    x = [[row[-1]] for row in augmented_matrix]
    return x

if __name__ == '__main__':
    A = [[4,1,1], [1, 2, -2], [1, 2, 3]]
    b = [[6], [9], [10]]
    x = gauss_jordan(A,b)
    print('Gaussian-Jordan elimination:')
    print("A=", A)
    print("b=", b)
    print("x=", x)