from collections import Counter

text = "I love natural language processing and I love Python"
words = text.lower().split()

vocab = set(words)
V = len(vocab)

unigram_count = Counter(words)
total_words = len(words)

print("Smoothed Unigram Probabilities:")
for word in vocab:
    print(word, ":", (unigram_count[word] + 1) / (total_words + V))

bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
bigram_count = Counter(bigrams)

print("\nSmoothed Bigram Probabilities:")
for (word1, word2), count in bigram_count.items():
    print(f"P({word2}|{word1}) =", (count + 1) / (unigram_count[word1] + V))