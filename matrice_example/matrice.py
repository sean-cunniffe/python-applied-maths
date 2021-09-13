# 1. Modify the code to calculate the average value for all values in the matrix
# 2. Create a new Java file, based on this example, to
# a. Generate two random 3x3 matrices stored in A and B
# b. Multiply the matrices together (use the pseudo algorithm in notes)
# c. Print the result
# d. Use methods
import random


def generate_matrix(dim, num_range):
    mat = [[0 for _ in range(dim)] for _ in range(dim)]
    for r in range(dim):
        for c in range(dim):
            num = random.randint(0, num_range)
            mat[r][c] = num
    return mat


# get sum of all values of a matrix
def get_sum(mat):
    cnt = 0
    for row1 in mat:
        for col1 in row1:
            cnt = cnt + col1
    return cnt


def multiple_matrix(mat1, mat2):
    result_mat = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    mat2 = transpose_matrix(mat2)

    for index_i, i in enumerate(result_mat):
        for index_j, _ in enumerate(i):
            result_mat[index_i][index_j] = multiply_arr(mat1[index_i], mat2[index_j])

    return result_mat


# transpose matrix so easier when multiplying rows and columns, we just multiply row by row
def transpose_matrix(mat):
    transposed = [[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]
    for index_i, i in enumerate(mat):
        for index_j, _ in enumerate(i):
            transposed[index_i][index_j] = mat[index_j][index_i]
    return transposed


# multiply two arrays and sums values
def multiply_arr(arr1, arr2):
    sum1 = 0
    for index, val1 in enumerate(arr1):
        sum1 += val1 * arr2[index]
    return sum1
