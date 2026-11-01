# (a) Morpheme segmentation
words = {
    "un + happy + ness": "unhappiness",
    "teach + er + s": "teachers",
    "dis + establish + ment": "disestablishment",
    "inter + nation + al + ize + ation": "internationalization"
}
for word, result in words.items():
    print(word, "->", result)
# (b) Number of morphemes
print("unhappiness -> 3 morphemes")
print("teachers -> 3 morphemes")
print("disestablishment -> 3 morphemes")
print("internationalization -> 5 morphemes")
# (c) Suffix classification
print("ness -> Derivational")
print("er -> Derivational, s -> Inflectional")
print("ment -> Derivational")
print("al, ize, ation -> Derivational")
# (d) Morpheme types
print("Prefixes: un, dis, inter")
print("Roots: happy, teach, establish, nation")
print("Suffixes: ness, er, s, ment, al, ize, ation")
