subjects=["students"]
verb=["borrows", "returns"]
object=["book"]
for s in subjects:
    for v in verb:
        for o in object:
            print(s, v, o)