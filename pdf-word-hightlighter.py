import sys
import fitz
import argparse
import json

parser = argparse.ArgumentParser(description='Automatically highlight keywords in a PDF')
parser.add_argument('pdf', help="path to the pdf")
parser.add_argument('-w', '--word', help="word to highlight, can be called multiple times", required=False, default=[], action='append')
parser.add_argument('-wl', '--wordlist', help="path to .txt file with one or more words on every line to be searched", required=False, action='append') 
parser.add_argument('-o', '--output', help="optional output file name, will default to prepending 'marked-' to the original pdf", required=False, default = [])
parser.add_argument('-c','--color', help="optional argument to specify the color of the highlights. If more than one input word(list) is provided, the colors will be applied in the same order as the input word(lists), defaulting to yellow if the specified colors >2 but <#wordlists. If multiple wordlists are provided but only one color, that color will be applied to all. Defaults to yellow. Options: red, blue, green, yellow; or RGB color value in the form [X.X, X.X, X.X]", action='append')


def mark_word(page, text, color):
	#print(color)
	found = 0
	#wlist = page.getTextWords()
	#for w in wlist:
	#	if text in w[4]:
	#		found += 1
	#		r = fitz.Rect(w[:4])
	#		page.addHighlightAnnot(r)
	wlist = page.searchFor(text)
	annot=page.addHighlightAnnot(wlist)
	annot.set_colors(stroke=color)
	annot.update(opacity=0.4, fill_color=[0.0,1.0,0.0])
	found = len(wlist)
	return found

argument = parser.parse_args()

colors=argument.color

fname = argument.pdf
wordlist = argument.wordlist
listlist= []
if wordlist:
	for l in wordlist:
		text=[]
		with open(l, "r") as f:
			text = f.read().splitlines()
		listlist.append(text)
w = argument.word


doc = fitz.open(fname)
if not colors:
	colors=["yellow"]
cols=["yellow", "magenta", "cyan","red", "green", "blue"]
rgbs=[[1,1,0],[1,0,1],[0,1,1],[1,0,0],[0,1,0],[0,0,1]]
for ix, color in enumerate(colors):
	if color[0]!="[":
		if color in cols:
			colors[ix]=rgbs[cols.index(color)]
	else:
		colors[ix]=json.loads(color)

length = len(w)+len(listlist)

if length>len(colors):
	if len(colors)==1:
		for i in range(0, length>len(colors)):
			colors.append(colors[0])
	else:
		for i in range(0, length-len(colors)):
			colors.append([1,1,0])
if length<len(colors):
	colors=colors[:(len(colors)-1)]


new_doc = False

for page in doc:
	if w:
		for index,word in enumerate(w):
			found=mark_word(page,word, colors[index])
			if found:
				new_doc=True	
	if wordlist:
		for index, wl in enumerate(listlist):
			for word in wl:
				found = mark_word(page, word, colors[index])
				if found:
					new_doc = True
				#print("found '%s' %i times on page %i" % (text, found, page.number + 1))

if new_doc:
	if argument.output:
		if argument.output[-4:]==".pdf":
			doc.save(argument.output)
		else:
			doc.save(argument.output + ".pdf")
	else:
		doc.save("marked-" + doc.name)
