import re

def countWords(wordLst):
    dict = {}
    for word in wordLst:
        if word in dict:
            dict[word] = dict[word] +1
        else:
            dict[word] = 1
    return len(dict.keys())

              
 
def main():

    fin = open("middlemarch",'r')
    data = fin.read()
    data = re.sub('\n',' ',data)
    wordLst = data.split()
    count = countWords(wordLst)

    print(count)
   
main()
