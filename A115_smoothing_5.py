words = {
    "glasses": ["without", "reading", "my"],
    "Francisco": ["San"]
}
for word, previous_words in words.items():
    print(word, "distinct previous words:", len(previous_words))
print("Preferred word: glasses")