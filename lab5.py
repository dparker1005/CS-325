import nltk
from nltk.corpus import treebank
from nltk.tree import Tree

#I have decided to only include translations for words that are different in Spanish than they are in English
translationsToSpanish = {"years":"anos", "old":"viejo", "will":"va a", "join":"unirse","the":"la", "board":"junta", "as":"como", "a":"un", "nonexecutive":"no ejecutivo", "director":"director" }

def makeSyntacticTransfer(tree, rootPOS, firstChildPOS, secondChildPOS, translate): #translate is boolean, True translates to Spanish
	numChildren = len(tree)
	if tree.label() == rootPOS:
		tempVar = False
		for index in range(0,numChildren):
			if(tree[index].label()==secondChildPOS and tempVar == True):
				tempTree = tree[index-1]
				tree[index-1] = tree[index]
				tree[index] = tempTree
			tempVar = False
			if(tree[index].label()==firstChildPOS):
				tempVar = True
	if tree.height()>2:
		for index in range(0, numChildren):
			newTree = makeSyntacticTransfer(tree[index], rootPOS, firstChildPOS, secondChildPOS, translate)
			if newTree is not None:
				tree[index] = newTree
	elif translate==True:
		word = tree.leaves()[0]
		if translationsToSpanish.has_key(word):
			tree = Tree(tree.label(), [translationsToSpanish[word]])
		return tree

def prettyPrint(tree):
	tree.pretty_print()

def printSentence(tree):
	print tree.leaves()

def translateWord(word):
	for l in tree.leaves():
		if translationsToSpanish.has_key(l):
			l = translationsToSpanish[l]

print "File id's in treebank:"
print treebank.fileids()
print "\n\n"
print treebank.parsed_sents("wsj_0001.mrg")[0]
tree1 = treebank.parsed_sents("wsj_0001.mrg")[0]
tree2 = treebank.parsed_sents("wsj_0001.mrg")[0]
printSentence(tree1)

#Original tree, no modifications
prettyPrint(tree1)

#Only reordering of tree, no translation. Shows complete lab without extra credit
makeSyntacticTransfer(tree1, "S", "NP-SBJ", "VP", False)
prettyPrint(tree1)

#Reordering of tree and translation. Shows complete lab with extra credit
makeSyntacticTransfer(tree2,"NP", "JJ", "NN", True)
prettyPrint(tree2)
