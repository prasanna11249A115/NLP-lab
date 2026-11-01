import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentences = [
    "The teacher is in the lab.",
    "A clever student reads a paper.",
    "The students work in the library."
]
grammar = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
VP: {<VB.*>+}
PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    print("\nSentence:", sentence)
    print(chunker.parse(tagged_words))
