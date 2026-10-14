import re
from collections import defaultdict
from nltk.probability import FreqDist

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(sentence):
    sentence = sentence.lower()
    return [""] + re.findall(r"[a-z']+", sentence) + [""]

sentences = [tokenize(s) for s in corpus.strip().split("\n")]

bigram_counts = defaultdict(FreqDist)
for sent in sentences:
    for i in range(len(sent) - 1):
        bigram_counts[sent[i]][sent[i + 1]] += 1

bigram_probs = {}
for w1, fdist in bigram_counts.items():
    total = fdist.N()
    bigram_probs[w1] = {w2: count / total for w2, count in fdist.items()}

vocab = sorted(list(set(w for sent in sentences for w in sent)))

header = f"{'':<10}" + "".join(f"{w:<10}" for w in vocab)
print(header)
print("-" * len(header))

for w1 in vocab:
    row = f"{w1:<10}"
    for w2 in vocab:
        prob = bigram_probs.get(w1, {}).get(w2, 0.0)
        row += f"{prob:<10.2f}"
    print(row)