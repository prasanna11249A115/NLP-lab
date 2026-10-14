subjects=["patients"]
verbs=["visits", "meet"]
objects=["doctor", "nurse"]
for s in subjects:
    for v in verbs:
        for o in objects:
            print(s, v, o)