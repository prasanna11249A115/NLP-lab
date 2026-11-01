
N = 45
T = 20
brute = N ** T
viterbi = T * N ** 2
print("Brute-force sequences: {:.2e}".format(brute))
print("Viterbi operations:", viterbi)