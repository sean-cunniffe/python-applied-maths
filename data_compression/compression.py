# Created By SEAN CUNNIFFE on 20/09/2021
import math as m
import numpy as np

N = 8
n = float(N)
T = np.zeros((N, N), dtype='float_')


def generate_t():
    for r in range(N):
        for c in range(N):
            if r is 0:
                T[r][c] = 1/m.sqrt(n)
            else:
                T[r][c] = m.sqrt(2.0/N) * np.cos(((2*r+1)*c*m.pi)/(2*n))


def main2():
    generate_t()
    print_matrix(T)


def print_matrix(array):
    for r in range(N):
        print(" ")
        for c in range(N):
            print("{0:0.3f}".format(array[r][c], end=' '))


if __name__ == '__main__':
    main2()
