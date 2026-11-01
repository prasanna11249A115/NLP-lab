import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentences = [
    "The student reads a book in the library.",
    "A teacher explains the lesson in class.",
    "The researchers develop a new model.",
    "Students play games on the ground.",
    "The professor works in the laboratory."
]
grammar = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
VP: {<MD>?<VB.*>+}
PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    print("\nSentence:", sentence)
    print(chunker.parse(tagged_words))
