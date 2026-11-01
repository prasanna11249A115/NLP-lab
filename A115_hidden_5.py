training_words = ["the", "dog", "barks", "a", "cat", "sleeps"]
word = "cats"
if word not in training_words:
    print("Unknown word:", word)
    print("Solution 1: Use an UNK token")
    print("Solution 2: Use suffix features")
print("Alternative model: Transformer")