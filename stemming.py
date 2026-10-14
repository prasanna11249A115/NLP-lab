from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("cars"))
print(stemmer.stem("children"))
print(stemmer.stem("running"))
print(stemmer.stem("better"))
print(stemmer.stem("studies"))
print(stemmer.stem("playing"))