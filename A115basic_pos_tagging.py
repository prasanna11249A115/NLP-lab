import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The intelligent student reads a book."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("Word\tPOS Tag")
print("-" * 25)
for word, tag in tagged_words:
    print(f"{word}\t{tag}")
