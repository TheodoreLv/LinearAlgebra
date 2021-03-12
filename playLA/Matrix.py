from playLA.Vector import Vector


class Matrix(object):

    def __init__(self, list2d):
        self._values = [list(row) for row in list2d]

    @classmethod
    def zero(cls, r, c):
        return cls([[0] * c for _ in range(r)])

    def row_vector(self, index):
        """返回矩阵的第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵的第index个列向量"""
        return Vector([row[index] for row in self._values])

    def __getitem__(self, index):
        return Vector(self.row_vector(index))

    @property
    def size(self):
        """返回矩阵元素的个数"""
        r, c = self.shape
        return r * c

    @property
    def row_num(self):
        """返回矩阵行数"""
        return self.shape[0]

    def __len__(self):
        return self.row_num

    @property
    def col_num(self):
        """返回矩阵列数"""
        return self.shape[1]

    @property
    def shape(self):
        """返回矩阵形状"""
        return len(self._values), len(self._values[0])

    @property
    def T(self):
        """返回矩阵的转置矩阵"""
        return Matrix([self.col_vector(i).list for i in range(self.col_num)])

    def __add__(self, other):
        """返回两个矩阵加法"""
        assert self.shape == other.shape, 'Error in adding, Shape must be same.'
        return Matrix([[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num)])

    def __sub__(self, other):
        """返回两个矩阵加法"""
        assert self.shape == other.shape, 'Error in subtracting, Shape must be same.'
        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num)])

    def dot(self, other):
        """返回两个矩阵乘法的结果"""
        if isinstance(other, Vector):
            assert self.col_num == len(other), 'Error in Matrix-Vector Multiplication'
            return Vector([self.row_vector(i).dot(other) for i in range(self.row_num)])
        if isinstance(other, Matrix):
            assert self.col_num == other.row_num, 'Error in Matrix-Matrix Multiplication'
            return Matrix([[self.row_vector(i).dot(other.col_vector(j)) for j in range(other.col_num)] for i in range(self.row_num)])

    def __mul__(self, other):
        """返回矩阵的数量乘法self*other"""
        return Matrix([[e * other for e in self.row_vector(i)] for i in range(self.row_num)])

    def __rmul__(self, other):
        """返回矩阵的数量乘法other*self"""
        return self * other

    def __truediv__(self, other):
        """返回矩阵的数量除法self/other"""
        return Matrix([[e / other for e in self.row_vector(i)] for i in range(self.row_num)])

    def __pos__(self):
        """返回矩阵取正的结果"""
        return 1 * self

    def __neg__(self):
        """返回矩阵取负的结果"""
        return -1 * self

    def __repr__(self):
        return 'Matrix({})'.format(self._values)

    __str__ = __repr__
