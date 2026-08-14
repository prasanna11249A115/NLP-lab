import re
from collections import Counter, defaultdict
corpus = """NLP subject is very interesting 
i love machine learning """
def tokenize(sentence):
    return ["<s>"] + re.findall(r"[a-z']+", sentence.lower()) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
unigram_counts = Counter()
bigram_counts = Counter()
vocab = set()
for sentence in sentences:
    unigram_counts.update(sentence[:-1])
    vocab.update(sentence)
    for i in range(len(sentence) - 1):
        bigram_counts[(sentence[i], sentence[i + 1])] += 1
prob_matrix = defaultdict(dict)
for w1 in vocab:
    for w2 in vocab:
        count = bigram_counts[(w1, w2)]
        if unigram_counts[w1] > 0:
            prob_matrix[w1][w2] = count / unigram_counts[w1]
        else:
            prob_matrix[w1][w2] = 0
words = sorted(vocab)
print("Bigram Probability Matrix")
print()
print(f"{'Word':<12}", end="")
for word in words:
    print(f"{word:<10}", end="")
print()
print("-" * (12 + 10 * len(words)))
for w1 in words:
    print(f"{w1:<12}", end="")
    for w2 in words:
        print(f"{prob_matrix[w1][w2]:<10.3f}", end="")
    print()