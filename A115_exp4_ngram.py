import re
import random
from collections import defaultdict, Counter
text = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
model = defaultdict(Counter)
for line in text.split("\n"):
    words = ["<s>"] + re.findall(r"[a-z']+", line.lower()) + ["</s>"]
    for i in range(len(words) - 1):
        model[words[i]][words[i + 1]] += 1
def generate():
    word = "<s>"
    sentence = []
    for i in range(15):
        next_words = model[word]
        if not next_words:
            break
        words = list(next_words.keys())
        counts = list(next_words.values())
        word = random.choices(words, weights=counts)[0]
        if word == "</s>":
            break
        sentence.append(word)
    return " ".join(sentence)
for i in range(3):
    print("Generated sentence:", generate())