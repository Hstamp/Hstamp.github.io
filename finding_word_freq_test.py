import collections
import os

os.chdir("C:\Users\H Stamp\Hstamp.github.io\speech_library")

speech_number = 364

while speech_number >= 1:

    wordcount = collections.Counter()
    with open (str(speech_number) + ".html", "r") as speech_file:
        for line in speech_file:
            wordcount.update(line.split())
        wordlist = ["the", "a", "is", "an", "it", "in", "and", "to"]

    for word in wordlist:
        if word in wordcount:
            del wordcount[word] #if "a" in wordcount:
        #del wordcount["a"]

    print 'Most common:'
    for letter, count in wordcount.most_common(20): #showing top 20 words
        print '%s: %d' % (letter, count)
    speech_file.close()
    speech_number -= 1
