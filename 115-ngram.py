import re, random
from collections import defaultdict, Counter
corpus = """NLP is very interesting subject regarding to AI"""
def tokenize(sentence):
    sentence = sentence.lower()
    return ["<s>"] + re.findall(r"[a-z']+", sentence) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
bigram_model = defaultdict(Counter)
for sent in sentences:
    for i in range(len(sent) - 1):
        bigram_model[sent[i]][sent[i + 1]] += 1
def generate_sentence(max_len=15):
    word = "<s>"
    result = []
    for _ in range(max_len):
        next_words = bigram_model[word]
        if not next_words:
            break
        words, counts = zip(*next_words.items())
        word = random.choices(words, weights=counts, k=1)[0]
        if word == "</s>":
            break
        result.append(word)
    return " ".join(result)
random.seed(42)
for i in range(3):
    print(f"Generated sentence {i+1}: {generate_sentence()}")