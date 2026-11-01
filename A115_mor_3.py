# (a) Over-stemming and under-stemming
print("Over-stemming: Unrelated words get the same stem.")
print("Example: university and universe")

print("Under-stemming: Related words get different stems.")
print("Example: alumnus and alumni")

# (b) Effects on search
print("Over-stemming -> Precision decreases")
print("Under-stemming -> Recall decreases")

# (c) Remedies
print("Use lemmatization and a legal dictionary.")
print("Use custom stemming rules and synonym lists.")
# (d) Simple solution
print("Match words using their meaning and context.")