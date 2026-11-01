import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Program 6 — Lab Activity 2: Manual Chunking
sentence = "The teacher explains the lesson in the classroom."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

grammar = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
VP: {<VB.*>+}
PP: {<IN><NP>}
"""

chunker = nltk.RegexpParser(grammar)
print(chunker.parse(tagged_words))
