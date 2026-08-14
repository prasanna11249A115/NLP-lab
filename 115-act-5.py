import re
import random
from collections import Counter, defaultdict
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    return ["<s>", "<s>"] + re.findall(
        r"[a-z']+", sentence.lower()
    ) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
bigram_model = defaultdict(Counter)
for sentence in sentences:
    for i in range(len(sentence) - 1):
        bigram_model[sentence[i]][sentence[i + 1]] += 1
def generate_bigram(max_len=15):
    word = "<s>"
    result = []
    for _ in range(max_len):
        choices = bigram_model[word]
        if not choices:
            break
        words, counts = zip(*choices.items())
        word = random.choices(
            words,
            weights=counts,
            k=1
        )[0]
        if word == "</s>":
            break
        result.append(word)
    return " ".join(result)
trigram_model = defaultdict(Counter)
for sentence in sentences:
    for i in range(len(sentence) - 2):
        context = (sentence[i], sentence[i + 1])
        next_word = sentence[i + 2]
        trigram_model[context][next_word] += 1
def generate_trigram(max_len=15):
    context = ("<s>", "<s>")
    result = []
    for _ in range(max_len):
        choices = trigram_model[context]
        if not choices:
            break
        words, counts = zip(*choices.items())
        next_word = random.choices(
            words,
            weights=counts,
            k=1
        )[0]
        if next_word == "</s>":
            break
        result.append(next_word)
        context = (context[1], next_word)
    return " ".join(result)
random.seed(42)
print("BIGRAM GENERATED SENTENCES")
print("-" * 35)
for i in range(3):
    print(f"{i + 1}. {generate_bigram()}")
print("\nTRIGRAM GENERATED SENTENCES")
print("-" * 35)
for i in range(3):
    print(f"{i + 1}. {generate_trigram()}")
print("\nOBSERVATION")
print("Bigram models consider one previous word.")
print("Trigram models consider two previous words.")
print("Therefore, trigram text is generally more context-aware and coherent.")