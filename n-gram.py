import re, random
from collections import defaultdict, Counter

corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

def tokenize(sentence):
    sentence = sentence.lower()
    return [""] + re.findall(r"[a-z']+", sentence) + [""]

sentences = [tokenize(s) for s in corpus.strip().split("\n")]

bigram_model = defaultdict(Counter)
for sent in sentences:
    for i in range(len(sent) - 1):
        bigram_model[sent[i]][sent[i + 1]] += 1

def generate_sentence(max_len=15):
    word = ""
    result = []
    for _ in range(max_len):
        next_words = bigram_model[word]
        if not next_words:
            break
        words, counts = zip(*next_words.items())
        word = random.choices(words, weights=counts, k=1)[0]
        if word == "":
            break
        result.append(word)
    return " ".join(result)

random.seed(42)
for i in range(3):
    print(f"Generated sentence {i+1}: {generate_sentence()}")