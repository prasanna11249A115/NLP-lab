import re
training_corpus = """NLP subject is very interesting 
i love machine learning"""
test_sentence = "the clever fox jumps over a house"
def tokenize(text):
    return re.findall(r"[a-z']+", text.lower())
training_tokens = tokenize(training_corpus)
training_vocab = set(training_tokens)
test_tokens = tokenize(test_sentence)
oov_words = [
    word for word in test_tokens
    if word not in training_vocab
]
oov_count = len(oov_words)
total_test_tokens = len(test_tokens)
oov_rate = oov_count / total_test_tokens
print("Training Vocabulary Size:", len(training_vocab))
print("Test Sentence:", test_sentence)
print("Total Test Tokens:", total_test_tokens)
print("OOV Words:", oov_words)
print("OOV Count:", oov_count)
print(f"OOV Rate: {oov_rate:.4f}")
print(f"OOV Rate (%): {oov_rate * 100:.2f}%")