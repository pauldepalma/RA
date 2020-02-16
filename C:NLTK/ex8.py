#Example 8 
#Use of an NLTK corpus
#Use of join which assembles a string from a list

import nltk   #use the previously installed nltk library
from nltk.corpus import gutenberg

def sentence(word):
    sentences = gutenberg.sents('melville-moby_dick.txt')
    for s in sentences:
        if word in s:
           print(' '.join(s)) 
           print()
    
def main():
    print("Press enter to see all sentences in Moby Dick with a chosen word")
    input()
    print("Enter a word")
    word = input()
    sentence(word)
main()
