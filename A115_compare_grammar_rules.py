import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The student reads a book in the library."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
grammar1 = r"NP: {<DT>?<JJ.*>*<NN.*>+}"
grammar2 = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
VP: {<MD>?<VB.*>+}
PP: {<IN><NP>}
"""
print("NP Only:")
print(nltk.RegexpParser(grammar1).parse(tagged_words))
print("\nNP + VP + PP:")
print(nltk.RegexpParser(grammar2).parse(tagged_words))
