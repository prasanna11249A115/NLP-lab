from collections import Counter

text = "I love natural language processing and I love Python"
words = text.lower().split()

grammar_rules = {
    "I": "Pronoun",
    "love": "Verb",
    "natural": "Adjective",
    "language": "Noun",
    "processing": "Noun",
    "and": "Conjunction",
    "Python": "Noun"
}

print("Grammar Based Model:")
for word in words:
    print(word, ":", grammar_rules.get(word.capitalize(), "Unknown"))

count = Counter(words)
total = len(words)

print("\nStatistical Model:")
for word in count:
    print(word, ":", count[word] / total)