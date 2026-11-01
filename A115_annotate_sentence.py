import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Program 7 — Lab Activity 3: Annotate a Sentence
sentence = "The young researcher develops an AI model."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

grammar = r"NP: {<DT>?<JJ.*>*<NN.*>+}"
chunker = nltk.RegexpParser(grammar)

print("POS Tags:", tagged_words)
print("Chunks:", chunker.parse(tagged_words))
