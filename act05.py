sentences=["i like to listen music", "i like watching movies", "i study nlp"]
word_freq={}
bigram_freq={}
for sentence in sentences:
    words=sentence.split()
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
for i in range(len(word)-1):
    bigram=words[i]+""+words[i+1]
    if bigram in bigram_freq:
        bigram_freq[bigram]+=1
    else:
        bigram_freq[bigram] = 1
print("word frequency:")
for word in word_freq:
    print(word,":",word_freq[word])
print("bigram frequency:")
for bigram in bigram_freq:
    print(bigram,":",bigram_freq[bigram])




