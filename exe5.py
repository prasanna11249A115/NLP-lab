import re
import random
from collections import defaultdict, Counter

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(sentence):

    sentence = sentence.lower()

    return (
        ["<s>", "<s>"]
        + re.findall(r"[a-z']+", sentence)
        + ["</s>"]
    )

sentences = [
    tokenize(s)
    for s in corpus.strip().split("\n")
]
bigram_model = defaultdict(Counter)

for sent in sentences:

    for i in range(len(sent) - 1):

        bigram_model[sent[i]][
            sent[i + 1]
        ] += 1
trigram_model = defaultdict(Counter)

for sent in sentences:

    for i in range(len(sent) - 2):

        trigram_model[
            (sent[i], sent[i + 1])
        ][sent[i + 2]] += 1


def generate_bigram(max_len=15):

    word = "<s>"

    result = []

    for _ in range(max_len):

        next_words = bigram_model[word]

        if not next_words:
            break

        words, counts = zip(
            *next_words.items()
        )

        word = random.choices(
            words,
            weights=counts,
            k=1
        )[0]

        if word == "</s>":
            break

        result.append(word)

    return " ".join(result)


def generate_trigram(max_len=15):

    w1 = "<s>"
    w2 = "<s>"

    result = []

    for _ in range(max_len):

        next_words = trigram_model[(w1, w2)]

        if not next_words:
            break

        words, counts = zip(
            *next_words.items()
        )

        w3 = random.choices(
            words,
            weights=counts,
            k=1
        )[0]

        if w3 == "</s>":
            break

        result.append(w3)

        w1 = w2
        w2 = w3

    return " ".join(result)


random.seed(42)

print("BIGRAM GENERATED TEXT")

for i in range(3):

    print(
        f"Sentence {i + 1}: "
        f"{generate_bigram()}"
    )


print("\nTRIGRAM GENERATED TEXT")

for i in range(3):

    print(
        f"Sentence {i + 1}: "
        f"{generate_trigram()}"
    )


print("\nObservation:")
print(
    "Trigram models generally produce more coherent "
    "sentences because they use two previous words "
    "to predict the next word."
)