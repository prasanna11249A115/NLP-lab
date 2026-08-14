import re
from collections import Counter
corpus = """NLP subject is very interesting 
i love machine learning"""
def tokenize(sentence):
    return ["<s>"] + re.findall(
        r"[a-z']+", sentence.lower()
    ) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
unigram_counts = Counter()
bigram_counts = Counter()
vocab = set()
for sentence in sentences:
    unigram_counts.update(sentence[:-1])
    vocab.update(sentence)
    for i in range(len(sentence) - 1):
        bigram_counts[
            (sentence[i], sentence[i + 1])
        ] += 1
V = len(vocab)
def bigram_probability(w1, w2, k=1.0):
    numerator = bigram_counts[(w1, w2)] + k
    denominator = unigram_counts[w1] + k * V
    return numerator / denominator
def sentence_probability(sentence, k=1.0):
    tokens = tokenize(sentence)
    probability = 1.0
    for i in range(len(tokens) - 1):
        probability *= bigram_probability(
            tokens[i],
            tokens[i + 1],
            k
        )
    return probability
test_sentence = "the fox runs away"
print("Sentence:", test_sentence)
print()
print(f"{'k value':<10}{'Probability':<20}")
print("-" * 30)
for k in [0.01, 0.1, 0.5, 1.0, 2.0]:
    probability = sentence_probability(
        test_sentence,
        k
    )
    print(f"{k:<10}{probability:<20.10f}")