import re
training_corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""

test_sentence = "the fox jumps over the cat"

def tokenize(text):

    return re.findall(
        r"[a-z']+",
        text.lower()
    )
training_words = tokenize(
    training_corpus
)
test_words = tokenize(
    test_sentence
)
training_vocabulary = set(
    training_words
)
oov_words = []
for word in test_words:
    if word not in training_vocabulary:

        oov_words.append(word)
oov_count = len(oov_words)
total_words = len(test_words)
oov_rate = oov_count / total_words
print("Test Sentence:", test_sentence)
print("Total test words:", total_words)
print("OOV words:", oov_words)
print("OOV count:", oov_count)
print(
    "OOV Rate:",
    round(oov_rate * 100, 2),
    "%"
)