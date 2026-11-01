import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The very intelligent student can read a book in the library."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
grammar = r"""
NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
VP: {<MD>?<VB.*>+}
PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
print("POS Tags:")
print(tagged_words)
print("\nImproved Chunk Tree:")
print(chunker.parse(tagged_words))
