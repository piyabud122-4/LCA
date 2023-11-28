def transpose(A):
    transposed_A = list(map(list, zip(*A)))
    return transposed_A

if __name__ == '__main__':
    A= [[1,2,3,4], [5,6,7,8], [9,10,11,12], [-1, -2, -3, -4]]
    At = transpose(A)
    print(A)
    print('is transposed to')
    print(At)