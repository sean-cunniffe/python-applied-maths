import numpy as np
import math


def haar_matrix(n, normalised):
    n = 2**np.ceil(np.log2(n))
    if n > 2:
        h = haar_matrix(n / 2, normalised)
    else:
        return np.array([[1, 1], [1, -1]])
    h_n = np.kron(h, [1, 1])  # calculate upper haar part, the first line in the matrix. I think this is usually all 1
    if normalised:
        h_i = np.sqrt(n/2)*np.kron(np.eye(len(h)), [1, -1])
    else:
        h_i = np.kron(np.eye(len(h)), [1, -1])
    h = np.vstack((h_n, h_i))  # combine parts
    return h


def RunNumericalExample(N, haar, normFlag):
    size = np.size(haar)
    reCompData = np.zeros(size)
    decompData = np.zeros(size)
    haar = haar_matrix(N, normFlag)

    # is 3 as the array is 8 in length. So there will be 3 levels on co-efficint "wall"
    # If the array was 16 digits long, the precision would be 4 - as there would be an extra row of getting average and co-efficient
    np.set_printoptions(precision=3)
    print("****** Haar Decomposition  ********")
    # data = np.random.randint(1,100, (1, N).ravel()
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Data: {0}".format(data))
    if normFlag ==True:
        decompData = (np.matmul(haar, data))/math.sqrt(N)
        for v in decompData:
            print("{0:0.3f}".format(v))
        print("********   ---------------------   ***************")
    else:
        print("The Haar matrix required by the Haar transform should be normalized \n"
              "This won't work, sorry....")
    haar = np.transpose(haar)
    if normFlag == True:
        reCompData = ((np.matmul(haar, decompData)) / (math.sqrt(N)))
        print("****** Haar Recomposition ******")
        print(reCompData)
        print("********   ---------------------   ***************")
    else:
        print("nothing in here")


def main():
    N = 8
    normFlag = True  # changed this from False to True, now it seems to work
    haar = haar_matrix(N, normFlag)
    np.set_printoptions(precision=3)  #this is 3, as there will be 3 lines in the co-efficient wall thing
    print("****** Haar Matrix (N={0}) ******".format(N))
    print(haar)
    print("****** ----------------------- ******".format(N))
    RunNumericalExample(N, haar, normFlag)


if __name__=='__main__':
    main()


