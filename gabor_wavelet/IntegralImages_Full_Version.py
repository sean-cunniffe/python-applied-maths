import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

class IntImage(object):
    def __init__(self, imageData):
        self.height, self.width = imageData.shape
        self.image = imageData
        self.IImage = np.copy(imageData)
        self.RIImage = np.zeros((self.height, self.width))

    def II(self):
        print("-------Integral Image-------")
        for r in range(1, self.height):
            self.IImage[r][0] += self.IImage[r-1][0]
        for c in range(1, self.width):
            self.IImage[0][c] += self.IImage[0][c-1]
        for r in range(1, self.height):
            for c in range(1, self.width):
                self.IImage[r][c]+=(self.IImage[r][c - 1] + self.IImage[r - 1][c]) - self.IImage[r - 1][c - 1];
        print(self.IImage.astype(int))
        self.normAndSave(self.IImage.astype(int), 0)


    def RII(self, rotation):
        self.RIImage[0][0] = self.image[0][0]
        print("-------Rotated II {0}-------".format(rotation))
        for r in range(self.height):
            for c in range(self.width):
                self.RIImage[r][c] = self.Sum(r,c, rotation)

        print(self.RIImage.astype(int))
        plt.imshow(self.RIImage.astype(int))
        plt.show()
        self.normAndSave(self.RIImage.astype(int), rotation)
 
    def Sum(self, y, x, rot):
        sumV = 0
        acrossX = x
        downY = y
        rotation = rot
        
        if rotation == 45:
            for i in range(downY, self.height):
                for j in range(0, acrossX+1):
                    sumV += self.image[i][j]
                acrossX -= 1

            for i in range(y-1, -1, -1):
                for j in range(x-1, -1, -1):
                    sumV += self.image[i][j]
                x -= 1

        if rotation == 135:
            for i in range(downY, self.height):
                for j in range(self.width-1, acrossX-1, -1):
                    sumV +=self.image[i][j]
                acrossX += 1

            for i in range(y-1, -1, -1):
                for j in range(x+1, self.width):
                    sumV += self.image[i][j]
                x+=1
            
        return sumV

    def CalculateSum(self, x, y, w, h):
        d = self.IImage[x+w][y+h]
        a = self.IImage[x][y]
        b = self.IImage[x][y+h]
        c = self.IImage[x+w][y]
        sum = d + a - b - c
        print(sum)

    def normAndSave(self, array, rotation):
        min = np.min(array)
        max = np.max(array)

        normImage = (array-min)/(max-min)*255
        outFile = Image.fromarray(normImage)
        outFile.convert('L').save("IntegralImage_{0}.png".format(rotation))


def DoTheWork(aMatrix):
    height, width = aMatrix.shape
    print(aMatrix)
    ii = IntImage(aMatrix)
    ii.II()
    ii.RII(45)
    ii.RII(135)

def main():
    print("----------Integral and Rotated Integral Image Generator----------")
    print("For demonstrational and computational reasons the width and height are going to be restricted to a maximum of 30 X 30")
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    if width<1 or width>30 or height<1 or height>30:
        print("Dimensions of this size are not accepted")
    else:
        option = input("Enter Y for a random matrix or N for a position matrix: ")

        if option.casefold() == 'y':
            print("Generating random matrix")
            randomMatrix = np.random.randint(1,10+1, size=(height, width))
            DoTheWork(randomMatrix)
        else:
            print("Generating position relative matrix")
            posMatrix = np.zeros((height, width))
            counter = 1
            for h in range(height):
                for w in range(width):
                    posMatrix[h][w] = counter
                    counter += 1
            DoTheWork(posMatrix)

if __name__=="__main__":
    main()

