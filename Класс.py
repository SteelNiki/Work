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


exec(stdin.read())
