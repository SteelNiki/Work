from sys import stdin
import copy


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

    def __add__(self, other):
        c = copy.deepcopy(other.lis)
        for i in range(len(self.lis)):
            for j in range(len(self.lis[i])):
                c[i][j] = c[i][j] + self.lis[i][j]
        return (Matrix(c))

    def __mul__(self, other):
        c = copy.deepcopy(self.lis)
        for i in range(len(c)):
            for j in range(len(c[i])):
                c[i][j] = (c[i][j] * other)
        return (Matrix(c))

    __rmul__ = __mul__


exec(stdin.read())
