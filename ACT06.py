from collections import Counter

corpus = [
    "I like NLP",
    "I like Python",
    "I enjoy NLP",
    "Python is powerful",
    "I like programming"
]

unigram_counts = Counter()
bigram_counts = Counter()

for sentence in corpus:
    words = sentence.split()
    unigram_counts.update(words)
    for i in range(len(words) - 1):
        bigram_counts[(words[i], words[i + 1])] += 1

def bigram_probability(sentence):
    words = sentence.split()
    probability = 1.0
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram_counts[bigram] == 0:
            return 0
        probability *= bigram_counts[bigram] / unigram_counts[words[i]]
    return probability

sentence1 = "I like NLP"
sentence2 = "Python like I"

p1 = bigram_probability(sentence1)
p2 = bigram_probability(sentence2)

print(sentence1, ":", p1)
print(sentence2, ":", p2)

if p1 > p2:
    print(sentence1, "is more probable")
else:
    print(sentence2, "is more probable")