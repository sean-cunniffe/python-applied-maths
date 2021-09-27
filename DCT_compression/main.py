from DCT_compression.DCT import DCT


def main():
    value = int(input("Select Quantisation level, Integer values only: "))
    dct = DCT(value)
    print('\nData to be compressed')
    dct.printMatrix(dct.M, 1)
    dct.calculate_FDCT()
    dct.quantizationStepForward()
    print('\n\nCompressed')
    dct.printMatrix(dct.C, 1)
    print('\n\n Decompressed Message')
    dct.QuantizationStepInverse()
    dct.calculate_IDCT()
    dct.printMatrix(dct.fin, 1)
    dct.compare()



if __name__ == '__main__':
    main()
