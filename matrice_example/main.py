# Created By SEAN CUNNIFFE on 13/09/2021
import matrice


def main():
    dimension = int(input('number of rows and columns?'))
    mat_size = dimension * dimension
    num_range = int(input('number range from 0 to ?'))

    mat1 = matrice.generate_matrix(dimension, num_range)
    mat2 = matrice.generate_matrix(dimension, num_range)
    mat1_average = matrice.get_sum(mat1) / mat_size
    mat2_average = matrice.get_sum(mat2) / mat_size

    print('Matrix 1:')
    for i in mat1:
        print(i)
    print('Average value =', mat1_average)
    print('\n')

    print('Matrix 2:')
    for i in mat2:
        print(i)
    print('Average value =', mat2_average)
    print('\n')

    result = matrice.multiple_matrix(mat1, mat2)

    for i in result:
        print(i)


if __name__ == '__main__':
    main()
