import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(text):
    return re.findall(
        r"[a-z']+",
        text.lower()
    )
words = tokenize(corpus)
unigram_counts = Counter(words)
bigram_counts = Counter()
for i in range(len(words) - 1):
    bigram_counts[
        (words[i], words[i + 1])
    ] += 1
V = len(set(words))
def add_k_probability(w1, w2, k):

    numerator = (
        bigram_counts[(w1, w2)] + k
    )

    denominator = (
        unigram_counts[w1] + k * V
    )

    return numerator / denominator


w1 = "the"
w2 = "fox"

print("Add-k Smoothing")
print("-" * 30)

for k in [0.01, 0.1, 0.5, 1.0, 2.0]:

    probability = add_k_probability(
        w1,
        w2,
        k
    )

    print(
        f"k = {k:<5}"
        f"P({w2}|{w1}) = "
        f"{probability:.6f}"
    )