from Execute import run

seq = ["brain.txt", "liver.txt", "muscle.txt"]

seq1 = int(input("Choose first Sequence(1 for brain, 2 for liver, 3 for muscle): "))
seq2 = int(input("Choose second Sequence(1 for brain, 2 for liver, 3 for muscle): "))

while (seq1 == seq2) or (not 1 <= seq1 <= 3) or (not 1 <= seq2 <= 3):
    print("Please Sequences must be deference and in range 1-3!")
    seq1 = int(input("Choose first Sequence(1 for brain, 2 for liver, 3 for muscle): "))
    seq2 = int(input("Choose second Sequence(1 for brain, 2 for liver, 3 for muscle): "))

run(seq[seq1 - 1], seq[seq2 - 1])


