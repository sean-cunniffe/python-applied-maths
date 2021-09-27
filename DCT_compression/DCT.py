import numpy as np
import math as math


class DCT(object):

    def __init__(self, level):
        self.N = 8
        self.n = 8.0
        self.T = np.zeros((self.N, self.N), dtype='float')
        self.Tt = np.zeros((self.N, self.N), dtype='float')
        self.DCT = np.zeros((self.N, self.N), dtype='float')
        self.TM = np.zeros((self.N, self.N), dtype='float')
        self.R = np.zeros((self.N, self.N), dtype='float')
        self.Q_Mat = np.zeros((self.N, self.N), dtype='int32')
        self.C = np.zeros((self.N, self.N), dtype='int32')
        self.fin = np.zeros((self.N, self.N), dtype='int32')

        self.q50 = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                             [12, 12, 14, 19, 26, 58, 60, 55],
                             [14, 13, 16, 24, 40, 57, 69, 56],
                             [14, 17, 22, 29, 51, 87, 80, 62],
                             [18, 22, 37, 56, 68, 109, 103, 77],
                             [24, 35, 55, 64, 81, 104, 113, 92],
                             [49, 64, 78, 87, 103, 121, 120, 101],
                             [72, 92, 95, 98, 112, 100, 130, 99]])

        self.M = np.array([[16, 8, 23, 16, 5, 14, 7, 22],
                           [20, 14, 22, 7, 14, 22, 24, 6],
                           [15, 23, 24, 23, 9, 6, 6, 20],
                           [14, 8, 11, 14, 12, 12, 25, 10],
                           [10, 9, 11, 9, 13, 19, 5, 17],
                           [8, 22, 20, 15, 12, 8, 22, 17],
                           [24, 22, 17, 12, 18, 11, 23, 14],
                           [21, 25, 15, 16, 23, 14, 22, 22]])

        self.Q_level = level
        self.generate_T()
        self.calculate_Q()

    def generate_T(self):
        for r in range(self.N):
            for c in range(self.N):
                if r == 0:
                    self.T[r][c] = 1 / math.sqrt(self.n)
                else:
                    self.T[r][c] = math.sqrt((2.0 / self.n)) * math.cos((r * math.pi*(2 * c + 1)) / (2 * self.n))
                self.Tt[c][r] = self.T[r][c]

    def calculate_Q(self):
        temp = 0
        if self.Q_level == 50:
            self.Q_Mat = np.copy(self.q50)
        elif self.Q_level >= 1 and self.Q_level < 50:
            for r in range(self.N):
                for c in range(self.N):
                    temp = int(self.q50[r][c] * (50 / self.Q_level))
                    if temp > 255:
                        self.Q_Mat[r][c] = 255
                    else:
                        self.Q_Mat[r][c] = temp
        elif self.Q_level > 50 and self.Q_level <= 100:
            for r in range(self.N):
                for c in range(self.N):
                    self.Q_Mat[r][c] = int(round(self.q50[r][c] * ((100 - float(self.Q_level)) / 50.0)))
        else:
            print("An invalid level was entered")
        self.printMatrix(self.Q_Mat, 1)

    def printMatrix(self, arr, arr_type):
        if arr_type == 0:
            for r in range(self.N):
                print(" "),
                for c in range(self.N):
                    print("{0:0.3f}".format(arr[r][c]), end=' ')
        if arr_type == 1:
            for r in range(self.N):
                print(" ")
                for c in range(self.N):
                    print('{0}'.format(arr[r][c]), end=' ')

    def calculate_FDCT(self):
        self.TM = np.matmul(self.T, self.M)
        self.DCT = np.matmul(self.TM, self.Tt)

    def calculate_IDCT(self):
        self.TM = np.matmul(self.Tt, self.R)
        self.fin = np.matmul(self.TM, self.T)

    def quantizationStepForward(self):
        self.C = np.divide(self.DCT, self.Q_Mat)

    def QuantizationStepInverse(self):
        self.R = np.multiply(self.C, self.Q_Mat)

    def compare(self):
        dif = np.abs(np.subtract(self.M, self.fin))
        print('\nDifference')
        self.printMatrix(dif, 0)

