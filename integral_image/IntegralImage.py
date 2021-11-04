import numpy as np
from matplotlib import pyplot as plt


class IntImage(object):
    def __init__(self, w, h, imageData, rotation):
        self.width = w
        self.height = h
        self.IImage = np.copy(imageData)
        self.rotation = rotation
        self.RII(rotation)

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

    def RII(self, rotation):
        # add the values of the row and update element value with current sum
        start, stop, step = (0, len(self.IImage[0]), 1) if rotation is 45 else (len(self.IImage[0]) - 1, -1, -1)
        for i, col in enumerate(self.IImage):
            total = 0
            for j in range(start, stop, step):
                row_val = col[j]
                total += row_val
                self.IImage[i][j] = total

        # start at top right and work way down column then across
        start, stop, step = (len(self.IImage[0]) - 1, -1, -1) if rotation is 45 else (0, len(self.IImage[0]), 1)
        j_direction = -1 if rotation == 45 else 1
        for element_j in range(start, stop, step):
            for element_i in range(len(self.IImage)):
                temp_i_index = element_i
                temp_j_index = element_j
                total = 0
                # diagonal values down and j_direction
                while len(self.IImage[0]) > temp_j_index >= 0 <= temp_i_index < len(self.IImage):
                    total += self.IImage[temp_i_index][temp_j_index]
                    temp_i_index += 1
                    temp_j_index += j_direction

                # diagonal values up and j_direction
                # equal the original position but move to
                # next position first as we already added the original position value
                temp_i_index = element_i - 1
                temp_j_index = element_j + j_direction
                while len(self.IImage[0]) > temp_j_index >= 0 <= temp_i_index < len(self.IImage):
                    total += self.IImage[temp_i_index][temp_j_index]
                    temp_i_index -= 1
                    temp_j_index += j_direction
                self.IImage[element_i][element_j] = total

    def CalculateRotatedSum(self, x, y, w, h, rotation):
        flip = -len(self.IImage[0]) if rotation == 135 else 0
        # TODO
        s1 = (x + (w - 1) + flip, y + (w - 1))
        s2 = (s1[0] + h + flip, s1[1] + h)
        s3 = (s2[0] + w + flip, s2[1] - w)
        s4 = (s3[0] - h + flip, s3[1] - h)
        # s1 = (x + (w - 1), y + (w - 1))
        # s2 = (s1[0] - h, s1[1] + h)
        # s3 = (s2[0] - w, s2[1] - w)
        # s4 = (s3[0] + h, s3[1] - h)
        b = self.IImage[s1[0]][s1[1]]
        d = self.IImage[s2[0]][s2[1]]
        c = self.IImage[s3[0]][s3[1]]
        a = self.IImage[s4[0]][s4[1]]
        print('%s+%s-%s-%s' % (d, a, b, c))
        return d + a - b - c

    def CalculateSum(self, x, y, w, h):
        d = self.IImage[x + w][y + h]
        a = self.IImage[x][y]
        b = self.IImage[x][y + h]
        c = self.IImage[x + w][y]
        print('%s+%s-%s-%s' % (d, a, b, c))
        sum = d + a - b - c
        return sum


def main():
    # image = np.random.randint(255, size=(8, 8))

    # image = [[184, 166, 150, 9, 57, 205, 119, 185],
    #          [14, 92, 42, 36, 174, 98, 115, 180],
    #          [67, 120, 82, 138, 113, 124, 106, 115],
    #          [134, 195, 1, 232, 111, 92, 28, 73],
    #          [49, 142, 30, 101, 108, 100, 175, 127],
    #          [123, 138, 13, 55, 146, 116, 170, 102],
    #          [53, 118, 24, 183, 216, 11, 126, 1],
    #          [137, 62, 115, 216, 55, 230, 7, 33]]
    image = [[185, 119, 205, 57, 9, 150, 166, 184],
             [180, 115, 98, 174, 36, 42, 92, 14],
             [115, 106, 124, 113, 138, 82, 120, 67],
             [73, 28, 92, 111, 232, 1, 195, 134],
             [127, 175, 100, 108, 101, 30, 142, 49],
             [102, 170, 116, 146, 55, 13, 138, 123],
             [1, 126, 11, 216, 183, 24, 118, 53],
             [33, 7, 230, 55, 216, 115, 62, 137]]

    # Random 2D array with values from 0 255
    # size = 10
    # image = []
    # for i in range(size):
    #     arr = []
    #     for j in range(size):
    #         arr.append(np.random.randint(0, 255))
    #     image.append(arr)
    rotation = 135

    ii1 = IntImage(len(image[0]), len(image), image, rotation)
    ii2 = ii1.IImage
    print(ii2)
    # 2675
    sum = ii1.CalculateRotatedSum(2, 1, 3, 4, rotation)
    print(sum)
    plt.imshow(ii2)
    plt.show()


if __name__ == "__main__":
    main()
