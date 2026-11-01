p_love = 0.7 * (2/3) + 0.3 * (3/17)
p_study = 0.7 * 0 + 0.3 * (1/17)
backoff_study = 0.4 * (1/17)
backoff_love = 2/3
print("Interpolated P(love | I):", round(p_love, 3))
print("Interpolated P(study | You):", round(p_study, 3))
print("Backoff score for study:", round(backoff_study, 3))
print("Backoff score for love:", round(backoff_love, 3))
