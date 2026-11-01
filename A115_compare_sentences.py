import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentences = [
    "The children are playing outside.",
    "She writes beautiful poems.",
    "They visited the library yesterday."
]
for sentence in sentences:
    print("\nSentence:", sentence)
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    print(tagged_words)
