import re
from collections import Counter
import matplotlib.pyplot as plt

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

words = re.findall(
    r"[a-z']+",
    corpus.lower()
)

unigram_counts = Counter(words)

top_10 = unigram_counts.most_common(10)

words = [
    item[0]
    for item in top_10
]

frequencies = [
    item[1]
    for item in top_10
]


plt.bar(
    words,
    frequencies
)

plt.xlabel("Words")

plt.ylabel("Frequency")

plt.title(
    "Top 10 Unigram Frequency Distribution"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.show()