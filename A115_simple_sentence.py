import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "Ravi plays cricket every evening."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
for word, tag in tagged_words:
    print(word, tag)
