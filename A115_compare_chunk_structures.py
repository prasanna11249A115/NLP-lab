import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
grammar = r"NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}"
chunker = nltk.RegexpParser(grammar)
sentences = [
    "a student",
    "the very intelligent student"
]
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    print("\nSentence:", sentence)
    print(chunker.parse(tagged_words))
