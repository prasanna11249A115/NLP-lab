import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Program 12 — Lab Activity 2: Extend the NP Rule
sentence = "The students read their textbooks."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

grammar = r"""
NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
VP: {<MD>?<VB.*>+}
PP: {<IN><NP>}
"""

chunker = nltk.RegexpParser(grammar)

print("POS Tags:", tagged_words)
print("\nChunk Tree:")
print(chunker.parse(tagged_words))
