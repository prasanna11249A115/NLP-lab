
# (a) Classify word pairs
words = {
    "walk + ed": "Inflection",
    "teach + er": "Derivation",
    "dog + s": "Inflection",
    "nation + al": "Derivation",
    "big + er": "Inflection",
    "quick + ly": "Derivation"
}
for word, result in words.items():
    print(word, "->", result)
# (b) Part-of-speech changes
print("teach -> teacher: Verb to Noun")
print("nation -> national: Noun to Adjective")
print("quick -> quickly: Adjective to Adverb")
# (c) Search engine conflation
print("walk, walked -> Conflate")
print("dog, dogs -> Conflate")
print("big, bigger -> Conflate")
# (d) Keep derivational forms separate
print("teach, teacher -> Keep separate")
print("nation, national -> Keep separate")
print("quick, quickly -> Keep separate")