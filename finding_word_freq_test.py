import collections

wordcount = collections.Counter()
with open ("strip_brexit_speech.txt", "r") as speech_file:
    for line in speech_file:
        wordcount.update(line.split())

print 'Most common:'
for letter, count in wordcount.most_common():
    print '%s: %d' % (letter, count)

#wordcount.iteritems():
#    print k, v

speech_file.close()
