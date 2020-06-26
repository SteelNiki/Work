from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, lis):
        self.lis = copy.deepcopy(lis)
        self.col = len(self.lis[0])
        self.row = len(self.lis)

    def __str__(self):
        str_lis = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.lis])
        return str_lis

    def size(self):
        return (self.row, self.col)

    def transpose(self):
        v = copy.deepcopy(self.lis)
        res = []
        n = len(v)
        m = len(v[0])
        for j in range(m):
            tmp = []
            for i in range(n):
                tmp = tmp + [v[i][j]]
            res = res + [tmp]
            self.lis = res
        return Matrix(self.lis)

    def __add__(self, other):
        c = copy.deepcopy(other.lis)
        if len(c) == len(self.lis) and len(c[0]) == len(self.lis[0]):
            for i in range(len(self.lis)):
                for j in range(len(self.lis[i])):
                    c[i][j] = c[i][j] + self.lis[i][j]
            return Matrix(c)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        c = copy.deepcopy(self.lis)
        for i in range(len(c)):
            for j in range(len(c[i])):
                c[i][j] = (c[i][j] * other)
        return (Matrix(c))

    __rmul__ = __mul__

    @staticmethod
    def transposed(mat):
        v = copy.deepcopy(mat.lis)
        res = []
        n = len(v)
        m = len(v[0])
        for j in range(m):
            tmp = []
            for i in range(n):
                tmp = tmp + [v[i][j]]
            res = res + [tmp]
        return Matrix(res)


exec(stdin.read())
