import re
from collections import Counter

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(sentence):
    sentence = sentence.lower()

    return (
        ["<s>", "<s>", "<s>"]
        + re.findall(r"[a-z']+", sentence)
        + ["</s>"]
    )

sentences = [
    tokenize(s)
    for s in corpus.strip().split("\n")
]

trigram_counts = Counter()
quadgram_counts = Counter()
vocab = set()

for sent in sentences:

    vocab.update(sent)

    for i in range(len(sent) - 3):

        trigram_counts[
            (sent[i], sent[i + 1], sent[i + 2])
        ] += 1

        quadgram_counts[
            (
                sent[i],
                sent[i + 1],
                sent[i + 2],
                sent[i + 3]
            )
        ] += 1

V = len(vocab)


def quadgram_prob(w1, w2, w3, w4):

    return (
        quadgram_counts[(w1, w2, w3, w4)] + 1
    ) / (
        trigram_counts[(w1, w2, w3)] + V
    )


print(f"{'Quadgram':<40}{'Count':<8}{'Probability':<15}")

print("-" * 63)

for quadgram, count in quadgram_counts.most_common(6):

    probability = quadgram_prob(*quadgram)

    print(
        f"{str(quadgram):<40}"
        f"{count:<8}"
        f"{probability:<15.4f}"
    )


def sentence_probability(sentence):

    tokens = tokenize(sentence)

    probability = 1.0

    for i in range(len(tokens) - 3):

        probability *= quadgram_prob(
            tokens[i],
            tokens[i + 1],
            tokens[i + 2],
            tokens[i + 3]
        )

    return probability


test = "the quick brown fox"

print(
    f'\nP("{test}") = '
    f'{sentence_probability(test):.10f}'
)