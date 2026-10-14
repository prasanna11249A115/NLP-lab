import re
from collections import Counter

corpus = """
Artificial intelligence is transforming the way people work and learn.
Machine learning systems can analyze large amounts of data.
Natural language processing helps computers understand human language.
Artificial intelligence is used in education, healthcare, finance and business.
Machine learning is becoming an important technology in modern society.
"""

def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)

words = tokenize(corpus)
unigram_counts = Counter(words)

print("TOP UNIGRAMS")
print("-" * 30)

for word, count in unigram_counts.most_common(10):

    probability = count / len(words)

    print(
        f"{word:<15}"
        f"{count:<8}"
        f"{probability:.4f}"
    )
bigram_counts = Counter()

for i in range(len(words) - 1):

    bigram_counts[
        (words[i], words[i + 1])
    ] += 1

print("\nTOP BIGRAMS")
print("-" * 30)

for bigram, count in bigram_counts.most_common(10):

    print(
        f"{bigram} : {count}"
    )
trigram_counts = Counter()

for i in range(len(words) - 2):

    trigram_counts[
        (
            words[i],
            words[i + 1],
            words[i + 2]
        )
    ] += 1

print("\nTOP TRIGRAMS")
print("-" * 30)

for trigram, count in trigram_counts.most_common(10):

    print(
        f"{trigram} : {count}"
    )