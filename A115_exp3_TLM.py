import re
from collections import Counter
text = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
bigram = Counter()
trigram = Counter()
vocab = set()
for line in text.split("\n"):

    words = re.findall(r"[a-z']+", line.lower())
    words = ["<s>", "<s>"] + words + ["</s>"]
    vocab.update(words)
    for i in range(len(words) - 2):
        bigram[(words[i], words[i + 1])] += 1
        trigram[(words[i], words[i + 1], words[i + 2])] += 1
V = len(vocab)
def probability(a, b, c):
    return (trigram[(a, b, c)] + 1) / (bigram[(a, b)] + V)
print("TRIGRAM       COUNT       PROBABILITY")
for t, count in trigram.most_common(6):
    p = probability(*t)
    print(t)
    print("Count       =", count)
    print("Probability =", round(p, 4))
    print()
test = ["<s>", "<s>", "the", "quick", "fox", "</s>"]
p = 1
for i in range(len(test) - 2):
    p *= probability(test[i], test[i + 1], test[i + 2])
print("Sentence Probability =", round(p, 10))