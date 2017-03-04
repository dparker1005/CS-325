import nltk
from nltk.book import *

#14484 english words in this corpus begin with the prefix 'un'
def findEnglishWordsWithPrefix(prefix):
	wordlist = set(nltk.corpus.words.words('en'))
	prefixedWords = []
	for word in wordlist:
		if word[0:len(prefix)]==prefix:
			prefixedWords+=[word]
	return prefixedWords

#It is clear that Sense and Sensibility has a much larger lexical diversity
#than Presidential Inaugural Addresses, which have larger lexical diversities
#than Monty Python and the Holy Grail. This makes sense because presidential
#canidates tend to use similar words often(such as country or freedom), and
#in Monty Python, people tend to talk in very similar ways and use the
#same words a lot.
def lexicalDiversity(text):
	return len(text)/len(set(text))

#Presidental inaugural addresses used the word 'the' much ore often than 
#Sense and Sensibility, but Sense and Sensiblity only used it a little
#more often than Monty Python. This may show that speeches tend to use that
#word more than books or movies, or this difference could just be due
#to the context in which the words were spoken.
def percentageUsed(word, text):
	return 100.00*text.count(word)/len(text)

print('\n\n')

#20
print 'Lexical Diversity for text2: '+str(lexicalDiversity(text2))
#14
print 'Lexical Diversity for text4: '+str(lexicalDiversity(text4))
#7
print 'Lexical Diversity for text6: '+str(lexicalDiversity(text6))

#2.72715714528%
print 'Percentage Use of \'the\' in text2: '+str(percentageUsed('the', text2))+'%'
#6.36840841253%
print 'Percentage Use of \'the\' in text4: '+str(percentageUsed('the', text4))+'%'
#1.76224435669%
print 'Percentage Use of \'the\' in text6: '+str(percentageUsed('the', text6))+'%'

#14484
print str(len(findEnglishWordsWithPrefix('un')))+' english words have the prefex \'un\''
#I hypothesize that more words will begin with the prefix 'pro' than 'anti'
#2310
print str(len(findEnglishWordsWithPrefix('pro')))+' english words have the prefex \'pro\''
#1078
print str(len(findEnglishWordsWithPrefix('anti')))+' english words have the prefex \'anti\''
#My hypothesis was correct, as shown by the results above each function call
