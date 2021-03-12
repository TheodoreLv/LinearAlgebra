from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [3, 4]])
    print('matrix is: {}'.format(matrix))
    print('matrix.size = {}'.format(matrix.size))
    print('matrix.shape = {}'.format(matrix.shape))
    print('len(matrix) = {}'.format(len(matrix)))
    print('matrix[0] = {}'.format(matrix[0]))
    print('matrix[0, 0] = {}'.format(matrix[0][0]))
    print('matrix.row_vector(1) = {}'.format(matrix.row_vector(1)))
    print('matrix.col_vector(1) = {}'.format(matrix.col_vector(1)))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print('add: {}'.format(matrix + matrix2))
    print('sub: {}'.format(matrix - matrix2))
    print('scalar-mul: {}'.format(matrix * 2))
    print('scalar-mul: {}'.format(2 * matrix))
    print('scalar-div: {}'.format(matrix / 2))
    print('zero_2_3: {}'.format(Matrix.zero(2, 3)))

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print('T.dot(p) = {}'.format(T.dot(p)))

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print('T.dot(P) = {}'.format(T.dot(P)))

    print('A.dot(B) = {}'.format(matrix.dot(matrix2)))
    print('B.dot(A) = {}'.format(matrix2.dot(matrix)))

    print('P = {}'.format(P))
    print('P.T = {}'.format(P.T))
