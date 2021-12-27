import math
import numpy as np


def findPath(res0, res1, z):
    r0 = 0
    r1 = 0

    if z == 0:
        r0 = res0 * 0.9
        r1 = res1 * 0.1
    elif z == 1:
        r0 = res0 * 0.1
        r1 = res1 * 0.9
    if r0 > r1:
        maxr = r0
    else:
        maxr = r1
    return maxr


def findSituation(seq, matrix):
    result0 = 0
    result1 = 0
    result00 = 0
    result11 = 0
    size = len(seq)
    situation = np.array([[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]])
    for x in range(size):
        if x == 0:
            if seq[x] == 'A':
                result00 = 0.5 * matrix[0][0]
                result11 = 0.5 * matrix[1][0]
            if seq[x] == 'G':
                result00 = 0.5 * matrix[0][1]
                result11 = 0.5 * matrix[1][1]

            if seq[x] == 'T':
                result00 = 0.5 * matrix[0][2]
                result11 = 0.5 * matrix[1][2]

            if seq[x] == 'C':
                result00 = 0.5 * matrix[0][3]
                result11 = 0.5 * matrix[1][3]

        else:
            if seq[x] == 'A':
                result00 = findPath(result0, result1, 0)
                result00 = result00 * matrix[0][0]
                result11 = findPath(result0, result1, 1)
                result11 = result11 * matrix[1][0]
            if seq[x] == 'G':
                result00 = findPath(result0, result1, 0)
                result00 = result00 * matrix[0][1]
                result11 = findPath(result0, result1, 1)
                result11 = result11 * matrix[1][1]
            if seq[x] == 'T':
                result00 = findPath(result0, result1, 0)
                result00 = result00 * matrix[0][2]
                result11 = findPath(result0, result1, 1)
                result11 = result11 * matrix[1][2]
            if seq[x] == 'C':
                result00 = findPath(result0, result1, 0)
                result00 = result00 * matrix[0][3]
                result11 = findPath(result0, result1, 1)
                result11 = result11 * matrix[1][3]

        result0 = result00
        result1 = result11
        math.log2(result0)
        situation[0][x] = math.log2(result0)
        situation[1][x] = math.log2(result1)
    state = ''

    print("Probabilities: ")
    for x in range(2):
        for y in range(size):
            print(situation[x][y], end=' | ')

    for x in range(size):
        if situation[0][x] > situation[1][x]:
            state = state + 'a'
        else:
            state = state + 'b'

    print("\nMost probable path is : " + state)


def main():
    matrix = np.array([[0.4, 0.4, 0.1, 0.1], [0.2, 0.2, 0.3, 0.3]])

    print("The table below show the possibly of each state (a & b) to produce the Nucleotides (A,G,T,C)\n States / "
          "Nucleotides:  A     G     T     C \n a)                    ", end='')

    for x in range(2):
        for y in range(4):
            print(matrix[x][y], "  ", end='')
        if x == 0:
            print("\n b)                 ", "  ", end='')

    print("\n")
    seq = 'GGCT'
    findSituation(seq, matrix)


main()
