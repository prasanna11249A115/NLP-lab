subjects=["students"]
verbs=["studies", "attend"]
object=["NLP","MATHS", "ENGLISH"]
for s in subjects:
    for v in verbs:
        for o in object:
            print(s, v, o)