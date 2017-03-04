import nltk
from nltk.book import *

def timesStringAppears(word):
	totalInstances = 0
	for x in inaugural.fileids():
		output = x[0:4]
		output +=  ' - '
		numTimes = inaugural.words(x).count(word)
		output +=  str(numTimes)
		totalInstances+=numTimes
		print output
	print 'Total - ' + str(totalInstances)

#function call
print('\n\n')
timesStringAppears('freedom')
