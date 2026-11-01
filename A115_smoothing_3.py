
N1 = 7
N2 = 2
N3 = 2
N = 17

print("N1:", N1)
print("N2:", N2)
print("N3:", N3)
print("Unseen probability mass:", round(N1/N, 3))

c1 = 2 * N2 / N1
c2 = 3 * N3 / N2

print("Adjusted count c*(1):", round(c1, 3))
print("Adjusted count c*(2):", round(c2, 3))

