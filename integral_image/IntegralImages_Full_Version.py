import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


class IntImage(object):
    def __init__(self, imageData):
        self.height, self.width = len(imageData), len(imageData[0])
        self.image = imageData
        self.IImage = np.copy(imageData)
        self.RIImage = np.zeros((self.height, self.width))

    def II(self):
        print("-------Integral Image-------")
        for r in range(1, self.height):
            self.IImage[r][0] += self.IImage[r - 1][0]
        for c in range(1, self.width):
            self.IImage[0][c] += self.IImage[0][c - 1]
        for r in range(1, self.height):
            for c in range(1, self.width):
                self.IImage[r][c] += (self.IImage[r][c - 1] + self.IImage[r - 1][c]) - self.IImage[r - 1][c - 1];
        print(self.IImage.astype(int))
        self.normAndSave(self.IImage.astype(int), 0)

    def RII(self, rotation):
        self.RIImage[0][0] = self.image[0][0]
        print("-------Rotated II {0}-------".format(rotation))
        for r in range(self.height):
            for c in range(self.width):
                self.RIImage[r][c] = self.Sum(r, c, rotation)

        print(self.RIImage.astype(int))
        plt.imshow(self.RIImage.astype(int))
        plt.show()
        sum = self.CalculateRotatedSum(2, 1, 3, 4)
        print(sum)
        self.normAndSave(self.RIImage.astype(int), rotation)

    def CalculateRotatedSum(self, x, y, w, h):
        s1 = (x + (w - 1), y + (w - 1))
        s2 = (s1[0] - h, s1[1] + h)
        s3 = (s2[0] - w, s2[1] - w)
        s4 = (s3[0] + h, s3[1] - h)
        b = self.IImage[s1[0]][s1[1]]
        d = self.IImage[s2[0]][s2[1]]
        c = self.IImage[s3[0]][s3[1]]
        a = self.IImage[s4[0]][s4[1]]
        print('%s+%s-%s-%s' % (d, a, b, c))
        return d + a - b - c

    def Sum(self, y, x, rot):
        sumV = 0
        acrossX = x
        downY = y
        rotation = rot

        if rotation == 45:
            for i in range(downY, self.height):
                for j in range(0, acrossX + 1):
                    sumV += self.image[i][j]
                acrossX -= 1

            for i in range(y - 1, -1, -1):
                for j in range(x - 1, -1, -1):
                    sumV += self.image[i][j]
                x -= 1

        if rotation == 135:
            for i in range(downY, self.height):
                for j in range(self.width - 1, acrossX - 1, -1):
                    sumV += self.image[i][j]
                acrossX += 1

            for i in range(y - 1, -1, -1):
                for j in range(x + 1, self.width):
                    sumV += self.image[i][j]
                x += 1

        return sumV

    def CalculateSum(self, x, y, w, h):
        d = self.RIImage[x + w][y + h]
        a = self.RIImage[x][y]
        b = self.RIImage[x][y + h]
        c = self.RIImage[x + w][y]
        sum = d + a - b - c
        print(sum)

    def normAndSave(self, array, rotation):
        min = np.min(array)
        max = np.max(array)

        normImage = (array - min) / (max - min) * 255
        outFile = Image.fromarray(normImage)
        outFile.convert('L').save("IntegralImage_{0}.png".format(rotation))


def DoTheWork(aMatrix):
    print(aMatrix)
    ii = IntImage(aMatrix)
    ii.II()
    # ii.RII(45)
    ii.RII(135)
    print(sum)


def main():
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
    DoTheWork(image)


if __name__ == "__main__":
    main()
