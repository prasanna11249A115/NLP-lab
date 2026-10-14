import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "student" : ["alice","bobs","charlie","diana","frank","henry","jack","tinku","vyshali","bhavya"],
    "Math" : [92,78,91,90,88,85,83,98,99,96],
    "Science" : [78,95,99,96,94,88,82,84,92,91],
    "English" : [78,98,97,98,94,93,92,95,96,99],
    "Age" : [18,19,20,17,21,19,18,21,20,19],
    "Hours Studied" : [1,7,4,3,6,9,2,5,4,2],
       }
df = pd.DataFrame(data)
print(df.head())
plt.figure(figsize=(10,5))
plt.plot(df["student"], df["Math"],market="o",label="Math",color="blue")
plt.plot(df["student"], df["Science"],market="s",label="Science",color="green")
plt.plot(df["student"], df["English"],market="^",label="English",color="red")
plt.title("student score trends",fontsize=14)
plt.xlabel("student")
plt.ylabel("marks")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png",dpi=150)
plt.show()