import collections
import os

os.chdir("C:\Users\H Stamp\Documents\GitHub\Hstamp.github.io\speech_library")

speech_number = 364

while speech_number >= 1:

    wordcount = collections.Counter()
    with open (str(speech_number) + ".html", "r") as speech_file:
        for line in speech_file:
            wordcount.update(line.split())
            wordlist = ["were", "But", "should", "</div>", "<div", "/>", "do", "<a", "do", "We", "while", "those", "very", "most", "am", "some", "into", "hoc", "ad", "one", "say", "such", "these", "upon", "when", "year", "<p><strong>The", "last", "other", "He", "can", "as", "he", "at", "has", "all", "what", "will", "may", "The", "or", "who", "if", "us", "from", "no", "It", "would", "been", "so", "<p>", "the", "a", "is", "an", "it", "in", "and", "to", "of", "but", "you", "And", "be", "are", "have", "by", "not", "must", "our", "I", "that", "type='text/css'", "of", "which", "that", "-", "this", "for", "we", "their", "they", "his", "on", "was", "with"]

    for word in wordlist:
        if word in wordcount:
            del wordcount[word] #if "a" in wordcount:
        #del wordcount["a"]

    with open("top_twenty_words.txt", "w") as f:
        f.write("Top 10 words from speech %s: \n" % speech_number)
        for letter, count in wordcount.most_common(10): #showing top 20 words
            f.write("%s: %d \n" % (letter, count))

    #with open("strip_brexit_speech.txt", "w") as f:
    #    f.write(text.encode('utf-8'))
    speech_file.close()
    speech_number -= 1
