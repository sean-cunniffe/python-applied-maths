from DCT_compression.DCT import DCT


def main():
    value = int(input("Select Quantisation level, Integer values only: "))
    dct = DCT(value)
    print("\n\nData to be compressed:")
    dct.printMatrix(dct.M), 1


if __name__ == '__main__':
    main()
