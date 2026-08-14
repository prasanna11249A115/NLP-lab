import re
from collections import Counter
import matplotlib.pyplot as plt
corpus = """NLP subject is very interesting 
i love machine learning"""
def tokenize(text):
    return re.findall(r"[a-z']+", text.lower())
tokens = tokenize(corpus)
unigram_counts = Counter(tokens)
top10 = unigram_counts.most_common(10)
words = [item[0] for item in top10]
counts = [item[1] for item in top10]
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color="skyblue")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Unigram Frequency Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()