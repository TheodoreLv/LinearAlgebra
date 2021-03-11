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
