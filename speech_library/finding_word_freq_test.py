import collections
import os
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

os.chdir("C:\Users\H Stamp\Documents\GitHub\Hstamp.github.io\speech_library")

speech_number = 364

while speech_number >= 1:

    wordcount = collections.Counter()
    with open (str(speech_number) + ".html", "r") as speech_file:
        for line in speech_file:
            wordcount.update(line.split())
            wordlist = ["<p>as", "<p>by", "&ndash;</p>", "We&rsquo;ve", "often", "down", "cheers.)", "actual", "been,", "all,", "<p>we&rsquo;re", "it,</p>", "that,</p>", "up.</p>", "yes", "no.", "day", "<p>&ldquo;So", "comes", "See", "all,", "back.</p>", "lot", "all,", "responsibility.</p>", "values.</p>", "<p>Or", "so.</p>", "Those", "do,", "<p>I'll", "though", "doesn&rsquo;t", "know,", "<li>our", "yet", "for.</p>", "that.</p>", "public.</p>", "<p>about", "<p>Let", "It&rsquo;&shy;s", "Democrats.</p>", "more,", "you.", "Yes,", "came", "With", "become", "war.", "war,", "been", "brought", "you,", "&lsquo;The", "us,", "<p>10", "<p>No", "do.", "Democrats.</p>", "Europe.</p>", "people&rsquo;s", "Because", "is,", "ought", "until", "whom", "isn&rsquo;t", "Wales.</p>", "within", "<p>Say", "I&rsquo;ve", "They&rsquo;re", "doesn&rsquo;t", "difference.</p>", "they&rsquo;ll", "18", "<p>How", 'Logo"', "ga", "[];", "<p>My", "<p>Above", "<p>One", "change.</p>", "let's", "Let", "These", "politics.</p>", "When", "us.", "<li>I", "No", "Let", "<p>No", "How", "She", "<em>(Applause)</em>", "along", "know,", "11", "<p>Why", "/>We", "/>&nbsp;<br", "/>But", "across",  "5", "ago", "Heath&rsquo;s", "took", "thing", "you.</p>", "why,", "<p>As", "18", "ago,", "Perhaps", "We&rsquo;re", "Europe.&nbsp;", "didn&rsquo;t", "them.", "As", "&lsquo;Yes&rsquo;", "Let", "shown", "us.", "already", "On", "show", "All", "perhaps", "ten", "given", "know,", "far", "<p>He", "cent,", "&lsquo;The", "world.&nbsp;", "within", "(Loud", "saw", "(Applause.)</p>", "<p><strong>A", "applause).", "hear.)</p>", "(Applause.)&nbsp;", "war.&nbsp;", "(cheers),", "(cheers)", "Now,", "be,", "too.</p>", "didn&rsquo;t", "us.</p>", "<p>When", "clear</p>", "<p>for", "clear,</p>", "here&rsquo;s", "<p>Together", "<p>We've", "started.</p>", "let's", "this.", "Now", "I&rsquo;d", "thing", "work.</p>", "government.</p>", "<p>&ldquo;And", "world&rsquo;s", "become", "When", "others", "<p>On", ",", "today.</p", "something", "came", "four", "and</p>", "<p>Of", "today.</p>", "<p>&middot;", "us.", "let's", "<p>My", "<p>He", "right.", "ten", "work.</p>", "isn't", "<p>Human", "us,", "Act.</p>", "<p>From", "crime.</p>", "when,", "too,", "Your", "met", "Now", "<p>Now", "is,", "<p>Not", "<p>which", "<p>...and", "went", "need", "can't", "<p>Your", "I&rsquo;m", "say,", "<p>&hellip;and", "we&rsquo;ll", "six", "away", "time", "(applause).</p>", "again", "hear)", "merely", "ask", "Britain.</p>", "<p>but", "<p>who", "<p>Your", "we&rsquo;re", "<p>It's", "country.</p>", "That's", "Our", "Not", "this,", "<p>Conference,", "actually", "we'll", "use", "doing", "10", "eleven", "<p>Well,", ".", "Where", "Mrs.", "people.</p>", "including", "we'll", "0px;", "/>The", "12", "five", "<p>Because", "<p>*****</p>", "<p>If", "<p>To", "<p>are", "<p>from", "yes.</p>", "<p>in", "you&rsquo;re", "own.</p>", "we've", "don't", "it's", "that's", "we&rsquo;ve", "can&rsquo;t", "<p>For",  "just", "all.</p>", "that&rsquo;s", "<p>Only", "<p>Join", "<p>You", "say:", "I've", "&mdash;", "I'm", "<p>Question:</p>", "<p>Mrs.", "&hellip;", "It's", "really", "Speech", "speech", "we're", "cent", "ever", "To", "we&rsquo;d", "it,", "<em>(Applause)</em></p>", "<p>There", "/>And", "<br", "</strong></p>", "keep", "end", "Government&rsquo;s", "him", "Who", "archive", "</p>", "For", "political", "party", "Party", "Political", "<p>So", "them.</p>", "<p>We&rsquo;re", "why", "they&rsquo;re", "me", "hear.)", "(Cheers)</p>", "(Cheers)&nbsp;","(applause)</p>", "<p>Mr.", "since", "off", "always", 'name="comments"', "<p", "(Applause)</p>", "<p>&lsquo;The",  "<p>&lsquo;I", "go", "said:", "(Laughter)&nbsp;", "once", "it.&nbsp;", "Well,", "cannot", "hear)" "<p>but", "why", "know", "think", "<p>that", "That&rsquo;&shy;s", "&nbsp;There", "That&rsquo;s", "Britain&rsquo;s",  "(Cheers.)</p>", "<p>What", "Or", "<p>Madam", "let", "we&rsquo;re" "it's", "Labour&rsquo;s", "<p>Mr", "making", "used", "<p>is", "(Hear,", "hear).", "does", "hear),", "hear.)&nbsp;", "(loud", "(Laughter.)&nbsp;", "<p>of", "/><br", "take", "got", "<p>That&rsquo;s", "don&rsquo;t", "</li>", "there&rsquo;s", "<p>the", "<p>and", "<p>that" "<p>but", "<p>we", "<p>who" "<p>It&rsquo;&shy;s", "<p>That&rsquo;&shy;s", "That&rsquo;&shy;s" "got", "that.", "<p>It&rsquo;&shy;s", "won&rsquo;t", "A", "done", "used", "look", "<p>That", "little", "If", "Britain&rsquo;s", "come", "This", "she", "&lsquo;we", 'style="text-decoration:', "It&rsquo;s", "whether", "<li>The", "Mr", "(Applause).</p>", "whose", "You", "did", "come", "that,", "best", "either", "many", "being", "during", "and,", "be," "whom", "week", "between", "seen", "regard", "ought" "thing", "her", "few", "like", "through", "without", "many", "years", "regard", "made", "You", "it&rsquo;s", "quite", "<p>They", "did", "<p>This", "||", "<body>", 'href="donate-a-speech.htm">Donate', "})();", "</body", "told", "-->", "Well", "_gaq", 'media="all"', "('https:'", 'content="Welcome', "<p>It&rsquo;s", "<p>They", "let&rsquo;s", "<p>&bull;", "get", "<p>Who", "<p>A", "...", "speech,", "<p>That" "<p>So", "<p>It", "tell", "where", "<p>Our", "find", "out", 'class="inner-content">', "<p>It" 'style="text-decoration:', "never", "days", "even", "your", "among", "same", "make", "every", "here", "see", "things", "way", "before", "&nbsp;The", "it.", "That", "too", "give", "because", 'rel="stylesheet"', 'type="text/css"', "var", "it.<p>", "So", "<!--", "it.</p>", "each", 'type="text/javascript"></script>', "might", "&nbsp;What", "which,", "(Cheers.)&nbsp;", "&nbsp;But", "put", "<p>We", "after", "shall", "per", "next", "said", "<link", "|", "up", "now", "back", "over", "under", "going", "There", "could", "three", "What",  "only", "still", "two", "<p>I", "both", "then", "&nbsp;We", "much", "<meta", "<p>But", "<script", "also", "&nbsp;I", "how", "=", "<p>In", "In", "They", "than", "about", "&ndash;", "any", "(hear,", "<p>to", "&nbsp;It", "We", "<span", "more", "<p>&nbsp;</p>", "them", "Mr.", "<div", "do", "had", "&ndash", "(hear", "want", "<p>And", "<p>The", "there", "had", "my", "its", "/>", "were", "But", "should", "</div>", "<div", "/>", "do", "<a", "do", "We", "while", "those", "very", "most", "am", "some", "into", "hoc", "ad", "one", "say", "such", "these", "upon", "when", "year", "<p><strong>The", "last", "other", "He", "can", "as", "he", "at", "has", "all", "what", "will", "may", "The", "or", "who", "if", "us", "from", "no", "It", "would", "been", "so", "<p>", "the", "a", "is", "an", "it", "in", "and", "to", "of", "but", "you", "And", "be", "are", "have", "by", "not", "must", "our", "I", "that", "type='text/css'", "of", "which", "that", "-", "this", "for", "we", "their", "they", "his", "on", "was", "with"]

    for word in wordlist:
        if word in wordcount:
            del wordcount[word] #if "a" in wordcount:
        #del wordcount["a"]

    with open("top_twenty_words.txt", "a+") as f:   # 'a' appends to a file without overwriting lines, '+' creates the file if it doesn't exist
    #need to delete the top_twenty_words.txt file each time before running, otherwise each time you run it you'll add more to the file
        f.write("Top 10 words from speech %s: \n" % str(speech_number))
        for letter, count in wordcount.most_common(10): #showing top 10 words
            f.write("%s: %d \n" % (letter, count))
        f.write("\n")  #new line after each speech

    speech_file.close()
    speech_number -= 1
