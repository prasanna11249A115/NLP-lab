import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The young scientist is developing a new application."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
grammar = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
VP: {<MD>?<VB.*>+}
PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
print("POS Tags:", tagged_words)
print("\nChunk Tree:")
print(chunker.parse(tagged_words))
