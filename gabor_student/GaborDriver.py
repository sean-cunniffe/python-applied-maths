from Gabor_Student import D2GaborWavelet


def main():
    # changing the gabor wavelet changes the size of the 2d wavelet
    wave_length = 75
    # changes the "direction" of the wavelet on the 2D space
    orientation = 0
    phase = 0
    # changes the envelope size when mapped to 2D space
    aspect_ratio = 1
    # makes troughs shallower then larger over 1, below on creates more waves
    bandwidth = 1
    size = 501
    gab = D2GaborWavelet(wave_length, orientation, phase, aspect_ratio, bandwidth, size)
    gab.RunGabor()
    gab.ShowColourWavelet()
    # gab.ShowGrayScaleWavelet()


if __name__ == "__main__":
    main()
