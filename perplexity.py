def perplexity(prob, n):
 return prob ** (-1 / n) if prob > 0 else float("inf")
test_sentence = "the fox runs away"
n = len(test_sentence.split())
uni_p = 0.0009 # from Exercise 1 (chain of unigram probs)
bi_p = 0.00021 # from Exercise 2 sentence_probability()
tri_p = 0.00007 # from Exercise 3 sentence_probability()
print("Unigram Perplexity:", round(perplexity(uni_p, n), 2))
print("Bigram Perplexity:", round(perplexity(bi_p, n), 2))
print("Trigram Perplexity:", round(perplexity(tri_p, n), 2))