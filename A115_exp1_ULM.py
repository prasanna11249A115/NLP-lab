import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
tokens = re.findall(r"[a-z']+", corpus.lower())
word_counts = Counter(tokens)
N = len(tokens)
print("Total tokens:", N)
print("\nWord\tCount\tProbability")
for word, count in word_counts.most_common():
    probability = count / N
    print(word, "\t", count, "\t", round(probability, 4))
word = "fox"
probability = word_counts[word] / N
print("\nP('fox') =", round(probability, 4))