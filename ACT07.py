from collections import Counter

text = "I love natural language processing and I love Python"
words = text.lower().split()

unigram_count = Counter(words)
total_words = len(words)

print("Unigram Probabilities:")
for word, count in unigram_count.items():
    print(word, ":", count / total_words)

bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
bigram_count = Counter(bigrams)

print("\nBigram Probabilities:")
for (word1, word2), count in bigram_count.items():
    print(f"P({word2}|{word1}) =", count / unigram_count[word1])