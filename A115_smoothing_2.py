
k = 0.1

p_before = 2 / 3
p_laplace = 3 / 11
p_addk = (2 + k) / (3 + k * 8)
p_study = (0 + k) / (1 + k * 8)

print("Before smoothing:", round(p_before, 3))
print("After add-one:", round(p_laplace, 3))
print("After add-k:", round(p_addk, 3))
print("P(study | You):", round(p_study, 3))

