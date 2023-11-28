def determinant(A):
    if len(A) == 1 and len(A[0]) == 1:
        return A[0][0]
    det = 0
    for j in range(len(A[0])):
        minor_matrix = [row[:j] + row[j+1:] for row in A[1:]]
        minor_det = determinant(minor_matrix)
        det += A[0][j] * ((-1) ** j) * minor_det
    return det

if __name__ == '__main__':
    A = [[3, 4, 5], [1, -1, 0], [8, 2, 7]]
    detA = determinant(A)
    B = [[1, 2, 3, 4], [-1, 0, 0.5, 9], [0, -6, 0.7, 0.5], [4, 4, 2, 1]]
    detB = determinant(B)
    C = [[3, 4, 5], [1, -1, 0], [-7, 7, 0]]
    detC = determinant(C)
    print('A =', A)
    print('det A =', detA)
    print('B =', B)
    print('det B =', detB)
    print('C =', C)
    print('det C =', detC)