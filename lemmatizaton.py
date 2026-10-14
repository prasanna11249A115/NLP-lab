from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cars"))
print(lemmatizer.lemmatize("children"))
print(lemmatizer.lemmatize("running", pos="v"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("playing", pos="v"))
print(lemmatizer.lemmatize("mice", pos="n"))
print(lemmatizer.lemmatize("wind", pos="v"))

