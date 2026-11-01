
# (a) Possible morphological analyses
words = {
    "flies": ["fly + Noun + Plural",
              "fly + Verb + Present tense"],
    "saw": ["see + Verb + Past tense",
            "saw + Noun + Tool"],
    "leaves": ["leaf + Noun + Plural",
               "leave + Verb + Present tense"]
}

for word, analyses in words.items():
    print("\n", word)
    for analysis in analyses:
        print(analysis)

# (b) Correct analysis in the sentence
print("\nSentence: Time flies like an arrow")
print("flies -> fly + Verb")

# (c) Component resolving ambiguity
print("A syntactic parser uses sentence context.")

# (d) Purpose
print("Select the correct meaning based on context.")