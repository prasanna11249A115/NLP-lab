
# (a) Morpheme segmentation
word = {
    "ev": "house",
    "ler": "plural",
    "imiz": "our",
    "den": "from"
}

for morpheme, meaning in word.items():
    print(morpheme, "->", meaning)

print("Complete word: evlerimizden")
print("Meaning: from our houses")

# (b) Vocabulary explosion
print("Turkish adds multiple suffixes to a root.")
print("This creates many different word forms.")

# (c) Alternative method
print("Use subword tokenization.")
print("Examples: BPE and WordPiece.")

# (d) Benefit
print("Subwords reduce vocabulary size.")
print("The same morphemes can be reused.")

