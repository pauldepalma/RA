#Example 7 
#Use of an NLTK corpus

import nltk   #use the previously installed nltk library
from nltk.corpus import gutenberg

def main():
    #display a list of the corpora available
    print("Press enter to see some of the available corpora")
    input()
    print("Here are some available corpora")
    for fileid in gutenberg.fileids():
        print(fileid)

main()
