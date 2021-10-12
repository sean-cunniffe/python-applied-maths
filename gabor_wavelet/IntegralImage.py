import numpy as np


class IntImage(object):
    def __init__(self, w, h, imageData):
        self.width = w
        self.height = h
        self.IImage = np.copy(imageData)
        self.RII()

    def II2(self):
        for r in range(1, self.width):
            self.IImage[r][0] += self.IImage[r - 1][0]
        for c in range(1, self.height):
            self.IImage[0][c] += self.IImage[0][c - 1]
        for r in range(1, self.width):
            for c in range(1, self.height):
                self.IImage[r][c] += (self.IImage[r][c - 1] + self.IImage[r - 1][c]) - self.IImage[r - 1][c - 1]

    def II(self):
        # add the values of the row and update element value with current sum
        for i, col in enumerate(self.IImage):
            total = 0
            for j, row_val in enumerate(col):
                total += row_val
                self.IImage[i][j] = total
        # add the values of the columns and update element value with current sum
        no_of_col = len(self.IImage[0])
        no_of_row = len(self.IImage)
        for i in range(no_of_col):
            total = 0
            for j in range(no_of_row):
                total += self.IImage[j][i]
                self.IImage[j][i] = total

    def RII(self):
        # add the values of the row and update element value with current sum
        for i, col in enumerate(self.IImage):
            total = 0
            for j, row_val in enumerate(col):
                total += row_val
                self.IImage[i][j] = total

        # start at top right and work way down column then across
        for element_j in range(len(self.IImage[0]) - 1, 0, -1):
            for element_i, col in enumerate(self.IImage):
                temp_i_index = element_i
                temp_j_index = element_j
                total = 0
                # diagonal values down and left
                while temp_j_index >= 0 and temp_i_index < len(col):
                    total += self.IImage[temp_i_index][temp_j_index]
                    temp_i_index += 1
                    temp_j_index -= 1

                # diagonal values up and left
                temp_i_index = element_i - 1
                temp_j_index = element_j - 1
                while temp_i_index >= 0 and temp_j_index >= 0:
                    total += self.IImage[temp_i_index][temp_j_index]
                    temp_i_index -= 1
                    temp_j_index -= 1
                self.IImage[element_i][element_j] = total

    def CalculateSum(self, x, y, w, h):
        d = self.IImage[x + w][y + h]
        a = self.IImage[x][y]
        b = self.IImage[x][y + h]
        c = self.IImage[x + w][y]
        sum = d + a - b - c
        return sum


def main():
    # image = np.random.randint(255, size=(8, 8))
    # image = [[69, 34, 13, 168, 203, 193, 187, 49],
    #          [246, 97, 99, 144, 207, 190, 206, 213],
    #          [247, 61, 207, 147, 239, 84, 28, 233],
    #          [102, 181, 38, 52, 72, 46, 122, 75],
    #          [170, 185, 39, 112, 19, 241, 81, 8],
    #          [169, 217, 201, 50, 1, 220, 115, 55],
    #          [35, 214, 5, 7, 170, 163, 114, 123],
    #          [224, 25, 191, 37, 66, 18, 202, 126]]
    image = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]]
    print(image)
    ii = IntImage(len(image[0]), len(image), image)
    # area = ii.CalculateSum(1, 1, 4, 4)
    print(ii.IImage)


if __name__ == "__main__":
    main()
