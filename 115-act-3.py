import re
from collections import Counter
corpus = """NLP subject is very interesting 
i love machine learning"""
def tokenize(sentence):
    words = re.findall(r"[a-z']+", sentence.lower())
    return ["<s>", "<s>", "<s>"] + words + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
trigram_counts = Counter()
quadgram_counts = Counter()
vocab = set()
for sentence in sentences:
    vocab.update(sentence)
    for i in range(len(sentence) - 3):
        trigram = tuple(sentence[i:i+3])
        quadgram = tuple(sentence[i:i+4])
        trigram_counts[trigram] += 1
        quadgram_counts[quadgram] += 1
V = len(vocab)
def quadgram_probability(w1, w2, w3, w4, smoothing=True):
    quadgram = (w1, w2, w3, w4)
    context = (w1, w2, w3)
    if smoothing:
        return (quadgram_counts[quadgram] + 1) / (
            trigram_counts[context] + V
        )
    denominator = trigram_counts[context]
    if denominator == 0:
        return 0
    return quadgram_counts[quadgram] / denominator
print(f"{'Quadgram':<40}{'Count':<8}{'Probability':<12}")
print("-" * 60)
for quadgram, count in quadgram_counts.most_common(8):
    probability = quadgram_probability(*quadgram)
    print(
        f"{str(quadgram):<40}"
        f"{count:<8}"
        f"{probability:<12.4f}"
    )
def sentence_probability(sentence):
    tokens = tokenize(sentence)
    probability = 1.0
    for i in range(len(tokens) - 3):
        probability *= quadgram_probability(
            tokens[i],
            tokens[i + 1],
            tokens[i + 2],
            tokens[i + 3]
        )
    return probability
test = "the quick brown fox"
print(f"\nP(\"{test}\") = {sentence_probability(test):.10f}")