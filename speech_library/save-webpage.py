# save-webpage.py
import urllib2

speech_num = 364

while speech_num >= 1:

    url = 'http://www.britishpoliticalspeech.org/speech-archive.htm?speech=%r' % speech_num

    response = urllib2.urlopen(url)
    webContent = response.read()

    f = open(str(speech_num) + '.html', 'w') #filename
    f.write(webContent)
    f.close
    speech_num -= 1
