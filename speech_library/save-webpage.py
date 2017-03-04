# save-webpage.py
import csv
import urllib2

#for loop to count all URLs up to no. 364
for i in range(365):
    url = 'http://www.britishpoliticalspeech.org/speech-archive.htm?speech=1'.format(i)
#use urllib2 to read the webpage
    response = urllib2.urlopen(url)
    webContent = response.read()
#save this webContent to an html fale named after i
    f = open(str(i) + '.html', 'w') #filename
    f.write(webContent)
    f.close
