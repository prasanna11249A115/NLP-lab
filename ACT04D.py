subjects=["customer"]
verb=["deposit", "withdraws"]
objects=["money"]
for s in subjects:
    for v in verb:
        for o in objects:
            print(s, v, o)