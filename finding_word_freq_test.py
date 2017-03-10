import collections
import os

os.chdir("C:\Users\Charis\Documents\GitHub\Hstamp.github.io\speech_library")

speech_number = 364

while speech_number >= 1:

    wordcount = collections.Counter()
    with open (str(speech_number) + ".html", "r") as speech_file:
        for line in speech_file:
            wordcount.update(line.split())
            wordlist = ["<p>which", "<p>...and", "went", "need", "can't", "<p>Your", "I&rsquo;m", "say,", "<p>&hellip;and", "we&rsquo;ll", "six", "away", "time", "(applause).</p>", "again", "hear)", "merely", "ask", "Britain.</p>", "<p>but", "<p>who", "<p>Your", "we&rsquo;re", "<p>It's", "country.</p>", "That's", "Our", "Not", "this,", "<p>Conference,", "actually", "we'll", "use", "doing", "10", "eleven", "<p>Well,", ".", "Where", "Mrs.", "people.</p>", "including", "we'll", "0px;", "/>The", "12", "five", "<p>Because", "<p>*****</p>", "<p>If", "<p>To", "<p>are", "<p>from", "yes.</p>", "<p>in", "you&rsquo;re", "own.</p>", "we've", "don't", "it's", "that's", "we&rsquo;ve", "can&rsquo;t", "<p>For",  "just", "all.</p>", "that&rsquo;s", "<p>Only", "<p>Join", "<p>You", "say:", "I've", "&mdash;", "I'm", "<p>Question:</p>", "<p>Mrs.", "&hellip;", "It's", "really", "Speech", "speech", "we're", "cent", "ever", "To", "we&rsquo;d", "it,", "<em>(Applause)</em></p>", "<p>There", "/>And", "<br", "</strong></p>", "keep", "end", "Government&rsquo;s", "him", "Who", "archive", "</p>", "For", "political", "party", "Party", "Political", "<p>So", "them.</p>", "<p>We&rsquo;re", "why", "they&rsquo;re", "me", "hear.)", "(Cheers)</p>", "(Cheers)&nbsp;","(applause)</p>", "<p>Mr.", "since", "off", "always", 'name="comments"', "<p", "(Applause)</p>", "<p>&lsquo;The",  "<p>&lsquo;I", "go", "said:", "(Laughter)&nbsp;", "once", "it.&nbsp;", "Well,", "cannot", "hear)" "<p>but", "why", "know", "think", "<p>that", "That&rsquo;&shy;s", "&nbsp;There", "That&rsquo;s", "Britain&rsquo;s",  "(Cheers.)</p>", "<p>What", "Or", "<p>Madam", "let", "we&rsquo;re" "it's", "Labour&rsquo;s", "<p>Mr", "making", "used", "<p>is", "(Hear,", "hear).", "does", "hear),", "hear.)&nbsp;", "(loud", "(Laughter.)&nbsp;", "<p>of", "/><br", "take", "got", "<p>That&rsquo;s", "don&rsquo;t", "</li>", "there&rsquo;s", "<p>the", "<p>and", "<p>that" "<p>but", "<p>we", "<p>who" "<p>It&rsquo;&shy;s", "<p>That&rsquo;&shy;s", "That&rsquo;&shy;s" "got", "that.", "<p>It&rsquo;&shy;s", "won&rsquo;t", "A", "done", "used", "look", "<p>That", "little", "If", "Britain&rsquo;s", "come", "This", "she", "&lsquo;we", 'style="text-decoration:', "It&rsquo;s", "whether", "<li>The", "Mr", "(Applause).</p>", "whose", "You", "did", "come", "that,", "best", "either", "many", "being", "during", "and,", "be," "whom", "week", "between", "seen", "regard", "ought" "thing", "her", "few", "like", "through", "without", "many", "years", "regard", "made", "You", "it&rsquo;s", "quite", "<p>They", "did", "<p>This", "||", "<body>", 'href="donate-a-speech.htm">Donate', "})();", "</body", "told", "-->", "Well", "_gaq", 'media="all"', "('https:'", 'content="Welcome', "<p>It&rsquo;s", "<p>They", "let&rsquo;s", "<p>&bull;", "get", "<p>Who", "<p>A", "...", "speech,", "<p>That" "<p>So", "<p>It", "tell", "where", "<p>Our", "find", "out", 'class="inner-content">', "<p>It" 'style="text-decoration:', "never", "days", "even", "your", "among", "same", "make", "every", "here", "see", "things", "way", "before", "&nbsp;The", "it.", "That", "too", "give", "because", 'rel="stylesheet"', 'type="text/css"', "var", "it.<p>", "So", "<!--", "it.</p>", "each", 'type="text/javascript"></script>', "might", "&nbsp;What", "which,", "(Cheers.)&nbsp;", "&nbsp;But", "put", "<p>We", "after", "shall", "per", "next", "said", "<link", "|", "up", "now", "back", "over", "under", "going", "There", "could", "three", "What",  "only", "still", "two", "<p>I", "both", "then", "&nbsp;We", "much", "<meta", "<p>But", "<script", "also", "&nbsp;I", "how", "=", "<p>In", "In", "They", "than", "about", "&ndash;", "any", "(hear,", "<p>to", "&nbsp;It", "We", "<span", "more", "<p>&nbsp;</p>", "them", "Mr.", "<div", "do", "had", "&ndash", "(hear", "want", "<p>And", "<p>The", "there", "had", "my", "its", "/>", "were", "But", "should", "</div>", "<div", "/>", "do", "<a", "do", "We", "while", "those", "very", "most", "am", "some", "into", "hoc", "ad", "one", "say", "such", "these", "upon", "when", "year", "<p><strong>The", "last", "other", "He", "can", "as", "he", "at", "has", "all", "what", "will", "may", "The", "or", "who", "if", "us", "from", "no", "It", "would", "been", "so", "<p>", "the", "a", "is", "an", "it", "in", "and", "to", "of", "but", "you", "And", "be", "are", "have", "by", "not", "must", "our", "I", "that", "type='text/css'", "of", "which", "that", "-", "this", "for", "we", "their", "they", "his", "on", "was", "with"]

    for word in wordlist:
        if word in wordcount:
            del wordcount[word] #if "a" in wordcount:
        #del wordcount["a"]

    with open("top_twenty_words%s.txt" % speech_number, "w" ) as f:
        f.write("Top 10 words from speech %s: \n" % speech_number)
        for letter, count in wordcount.most_common(20): #showing top 20 words
            f.write("%s: %d \n" % (letter, count))

    #with open("strip_brexit_speech.txt", "w") as f:
    #    f.write(text.encode('utf-8'))
    speech_file.close()
    speech_number -= 1
