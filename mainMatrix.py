from playLA.Matrix import Matrix

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [3, 4]])
    print('matrix is: {}'.format(matrix))
    print('matrix.size() = {}'.format(matrix.size()))
    print('matrix.shape() = {}'.format(matrix.shape()))
    print('len(matrix) = {}'.format(len(matrix)))
    print('matrix[0, 0] = {}'.format(matrix[0, 0]))
    print('matrix.row_vector(1) = {}'.format(matrix.row_vector(1)))
    print('matrix.col_vector(1) = {}'.format(matrix.col_vector(1)))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print('add: {}'.format(matrix + matrix2))
    print('sub: {}'.format(matrix - matrix2))
    print('scalar-mul: {}'.format(matrix * 2))
    print('scalar-mul: {}'.format(2 * matrix))
    print('scalar-div: {}'.format(matrix / 2))
