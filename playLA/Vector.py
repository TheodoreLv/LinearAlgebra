import math

from ._global import EPSILON


class Vector(object):

    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """返回dim维零向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        """返回单位向量"""
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero.")
        return Vector(self._values) / self.norm()

    def __add__(self, other):
        """向量加法"""
        assert len(self) == len(other), "Error in adding, Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量减法"""
        assert len(self) == len(other), "Error in subtracting, Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def dot(self, other):
        """返回向量的点乘（结果为标量）"""
        assert len(self) == len(other), "Error in dot product. Length of vectors mut be same."
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, k):
        """向量的数量乘法(self * k)"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """向量的数量乘法(k * self)"""
        return self * k

    def __truediv__(self, k):
        """返回向量的数量除法(self / k)"""
        return 1 / k * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, item):
        return self._values[item]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return 'playLA({})'.format(self._values)

    def __str__(self):
        return '({})'.format(', '.join(str(e) for e in self._values))
