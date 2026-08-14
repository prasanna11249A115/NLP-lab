import nltk
import re
from collections import Counter
nltk.download("gutenberg")
from nltk.corpus import gutenberg
text = gutenberg.raw("austen-emma.txt")
text = text[:50000]
tokens = re.findall(r"[a-z']+", text.lower())
print("Total tokens:", len(tokens))
print("Vocabulary size:", len(set(tokens)))
unigram_counts = Counter(tokens)
print("\nTop 10 Unigrams:")
print(f"{'Word':<15}{'Count':<10}{'Probability':<12}")
print("-" * 37)
N = len(tokens)
for word, count in unigram_counts.most_common(10):
    probability = count / N
    print(f"{word:<15}{count:<10}{probability:<12.6f}")
bigram_counts = Counter(
    zip(tokens, tokens[1:])
)
print("\nTop 10 Bigrams:")
print(f"{'Bigram':<35}{'Count':<10}")
print("-" * 45)
for bigram, count in bigram_counts.most_common(10):
    print(f"{str(bigram):<35}{count:<10}")
trigram_counts = Counter(
    zip(tokens, tokens[1:], tokens[2:])
)
print("\nTop 10 Trigrams:")
print(f"{'Trigram':<50}{'Count':<10}")
print("-" * 60)
for trigram, count in trigram_counts.most_common(10):
    print(f"{str(trigram):<50}{count:<10}")