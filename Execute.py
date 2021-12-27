def loadSeq(txtName):
    print("Loading sequence file " + txtName + "...")
    seqFile = open("./Sequences/" + txtName, "r")
    ls = seqFile.readlines()
    seq = []
    for line in ls:
        for letter in line:
            seq.append(letter)
    seqFile.close()
    return seq


def run(seq1, seq2):
    seq1 = loadSeq(seq1)
    seq2 = loadSeq(seq2)

    if len(seq2) > len(seq1):
        seq1, seq2 = seq2, seq1

    canWin = []
    winningRmv = []
    canWin.append(False)
    canWin.append(True)
    for i in range(2, len(seq1) + 1):
        for j in range(1, int((i / 2) + 1)):
            if not (canWin[j]) and not (canWin[i - j]):
                canWin.append(True)
                winningSplit = [j, i - j]
                winningRmv.append(winningSplit)
                break
        else:
            canWin.append(False)
    if canWin[-1] or canWin[len(seq2)]:
        print("A is the winner.")
    else:
        print("B is the winner.")
    print("Winning splits: ")

    for i in winningRmv:
        print(i)
