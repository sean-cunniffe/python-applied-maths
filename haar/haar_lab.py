# Created By SEAN CUNNIFFE on 04/10/2021
import numpy as np
import math as math


def haar_matrix(n, normalised):
    n = 2 ** np.ceil(np.log2(n))
    if n > 2:
        h = haar_matrix(n / 2, normalised)
    else:
        return np.array([[1, 1], [1, -1]])
    h_n = np.kron(h, [1, 1])  # calculate upper haar part, the first line in the matrix. I think this is usually all 1
    if normalised:
        h_i = np.sqrt(n / 2) * np.kron(np.eye(len(h)), [1, -1])
    else:
        h_i = np.kron(np.eye(len(h)), [1, -1])
    h = np.vstack((h_n, h_i))  # combine parts
    return h


def printCoeffients(title, data: []):
    print('---------' + title + '---------')
    for v in data:
        if isinstance(v, int):
            print(v)
        else:
            print("{0:0.3f}".format(v))


def main():
    dataRange = 100
    val = int(input('Input a value between 2 and 5 inclusive: '))
    if val < 2 or val > 5:
        print('invalid input')
        return
    n = 2 ** val
    print('Size of array: ', n)

    haar = haar_matrix(n, True)
    np.set_printoptions(precision=3)

    genData = np.random.randint(dataRange, size=n)
    # genData = [62, 78, 56, 71]
    printCoeffients('Data', genData)

    decomp = (np.matmul(haar, genData)) / math.sqrt(n)

    haar = np.transpose(haar)

    reComp = ((np.matmul(haar, decomp)) / (math.sqrt(n)))
    np.round(reComp, 0, reComp)
    reComp = reComp.astype(int)

    printCoeffients('decomposed', decomp)
    printCoeffients('composed', reComp)
    if (reComp == genData).all():
        print('Successful Recompose')


if __name__ == '__main__':
    main()
