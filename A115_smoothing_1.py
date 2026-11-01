
V = 8

p1 = (1 + 1) / (4 + V)
p2 = (0 + 1) / (1 + V)
p3 = (1 + 1) / (1 + V)
p4 = (3 + 1) / (3 + V)

print("P(You | <s>):", round(p1, 3))
print("P(study | You):", round(p2, 3))
print("P(NLP | study):", round(p3, 3))
print("P(</s> | NLP):", round(p4, 3))
print("Sentence probability:", round(p1*p2*p3*p4, 5))

