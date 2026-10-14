from nltk.probability import FreqDist

corpus = ["the", "cat", "sat", "on", "the", "mat", "the", "cat", "sleeps"]
fdist = FreqDist(corpus)
total_tokens = fdist.N()
unigram_probs = {word: count / total_tokens for word, count in fdist.items()}

for word, prob in unigram_probs.items():
    print(f"P('{word}') = {prob:.4f}")