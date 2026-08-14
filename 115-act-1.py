import re
import nltk
from nltk.probability import FreqDist
corpus = """NLP subject is very interesting 
i love machine learning"""
def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)
tokens = tokenize(corpus)
fdist = FreqDist(tokens)
N = len(tokens)
print("Total tokens:", N)
print(f"{'Word':<12}{'Count':<8}{'Probability':<12}")
print("-" * 32)
for word, count in fdist.most_common():
    probability = count / N
    print(f"{word:<12}{count:<8}{probability:<12.4f}")
word = "fox"
print(f"\nP('{word}') = {fdist[word] / N:.4f}")