from playLA.Vector import Vector


class Matrix(object):

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(cls, r, c):
        return cls([[0] * c for _ in range(r)])

    def row_vector(self, index):
        """返回矩阵的第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵的第index个列向量"""
        return Vector([row[index] for row in self._values])

    def __getitem__(self, pos):
        r, c = pos
        return self._values[r][c]

    def size(self):
        """返回矩阵元素的个数"""
        r, c = self.shape()
        return r * c

    def row_num(self):
        """返回矩阵行数"""
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        """返回矩阵列数"""
        return self.shape()[1]

    def shape(self):
        """返回矩阵形状"""
        return len(self._values), len(self._values[0])

    def __add__(self, other):
        """返回两个矩阵加法"""
        assert self.shape() == other.shape(), 'Error in adding, Shape must be same.'
        return Matrix([[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])

    def __sub__(self, other):
        """返回两个矩阵加法"""
        assert self.shape() == other.shape(), 'Error in subtracting, Shape must be same.'
        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])

    def __mul__(self, other):
        """返回矩阵的数量乘法self*other"""
        return Matrix([[e * other for e in self.row_vector(i)] for i in range(self.row_num())])

    def __rmul__(self, other):
        """返回矩阵的数量乘法other*self"""
        return self * other

    def __truediv__(self, other):
        """返回矩阵的数量除法self/other"""
        return Matrix([[e / other for e in self.row_vector(i)] for i in range(self.row_num())])

    def __pos__(self):
        """返回矩阵取正的结果"""
        return 1 * self

    def __neg__(self):
        """返回矩阵取负的结果"""
        return -1 * self

    def __repr__(self):
        return 'Matrix({})'.format(self._values)

    __str__ = __repr__
