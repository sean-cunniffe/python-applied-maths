# Created By SEAN CUNNIFFE on 19/10/2021
import math
import sys


class Huffman(object):

    def __init__(self, probabilities):
        self.probabilities = probabilities

    def huffman_encoding(self):
        # check if all probabilities sum to 1 and make return array of tuplets
        val = []
        total = 0
        for i, prob in enumerate(self.probabilities):
            total = total + prob[1]
            val.append([prob[0], ''])

        if round(total) != 1:
            print('Do not total to 1 {0}', total)
            return
        # keep going till we only have one value left in probabilities
        while len(self.probabilities) > 1:
            # get the first smallest and remove from probs
            index = get_smallest_index(self.probabilities)
            smallest1 = self.probabilities.pop(index)
            # get the next smallest and remove from probs
            index = get_smallest_index(self.probabilities)
            smallest2 = self.probabilities.pop(index)
            # go through letters and add 1 or 0 to there code i they're in smallest or second smallest
            for letter_and_code in val:
                if letter_and_code[0] in smallest1[0]:
                    letter_and_code[1] = '0' + letter_and_code[1]
                elif letter_and_code[0] in smallest2[0]:
                    letter_and_code[1] = '1' + letter_and_code[1]
            new_val = (smallest1[0]+smallest2[0], smallest1[1] + smallest2[1])
            self.probabilities.append(new_val)
        return val


def get_smallest_index(probabilities):
    smallest = probabilities[0][1]
    index = 0
    for i, val in enumerate(probabilities):
        if smallest > val[1]:
            smallest = val[1]
            index = i
    return index


if __name__ == '__main__':
    probabilities = [['a', 0.08], ['b', 0.1], ['c', 0.12], ['d', 0.15], ['e', 0.2], ['f', 0.35]]
    huffman = Huffman(probabilities)
    encodings = huffman.huffman_encoding()
    print(encodings)
