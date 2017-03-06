import collections

wordcount = collections.Counter()
with open ("strip_brexit_speech.txt", "r") as speech_file:
    for line in speech_file:
        wordcount.update(line.split())
    wordlist = ["the", "a", "is", "an", "it", "in", "and", "to"]

    for word in wordlist:
        if word in wordcount:
            del wordcount[word] #delete word from counter - to be improved
    #if "a" in wordcount:
        #del wordcount["a"]

print 'Most common:'
for letter, count in wordcount.most_common(20): #showing top 20 words
    print '%s: %d' % (letter, count)

speech_file.close()
