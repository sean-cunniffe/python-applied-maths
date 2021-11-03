# Created By SEAN CUNNIFFE on 20/10/2021
import numpy as np


def transpose_using_np(arr):
    return np.transpose(arr)


def manual_transpose(arr):
    trans = np.array([[0] * len(arr)] * len(arr))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            trans[i][j] = arr[j][i]
    return trans


if __name__ == '__main__':
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('******Array before transpose*******\n', arr)
    trans1 = transpose_using_np(arr)
    print('******NP transpose*******\n', trans1)
    trans2 = manual_transpose(arr)
    print('******Manual transpose*******\n', trans2)
