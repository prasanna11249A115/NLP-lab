import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    words = re.findall(r"[a-z']+", sentence.lower())
    return ["<s>"] + words + ["</s>"]
sentences = [tokenize(s) for s in corpus.split("\n")]
word_counts = Counter()
bigram_counts = Counter()
for sentence in sentences:
    word_counts.update(sentence[:-1])
    for i in range(len(sentence) - 1):
        pair = (sentence[i], sentence[i + 1])
        bigram_counts[pair] += 1
V = len(set(word for sentence in sentences for word in sentence))
def bigram_probability(w1, w2):
    count_bigram = bigram_counts[(w1, w2)]
    count_word = word_counts[w1]
    return (count_bigram + 1) / (count_word + V)
print("Bigram\t\tCount\tProbability")
for pair, count in bigram_counts.most_common(8):
    print(pair, "\t", count,
          "\t", round(bigram_probability(pair[0], pair[1]), 4))
def sentence_probability(sentence):
    tokens = tokenize(sentence)
    probability = 1
    for i in range(len(tokens) - 1):
        probability *= bigram_probability(tokens[i], tokens[i + 1])
    return probability
test = "the fox runs"
print("\nP('the fox runs') =" , round(sentence_probability(test), 10))