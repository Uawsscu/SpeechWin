import nltk
#nltk.download()

from textblob import TextBlob
blob = TextBlob("The titular threat of The Blob has always struck me as the ultimate movie monster.")
b = TextBlob("I like a cat.")
nltk
sentence = b.sentences[0]
for word, pos in sentence.tags:
    if pos == 'NN':
        print word+" >>N"
    if pos == 'VBP':
        print word.pluralize()+" >>vb"

    #print word+" "+pos

