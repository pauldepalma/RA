#Example 6

#use the regular expression library
import re
    
def main():
    fin = open("ex6.txt", 'r')

    #read file into one long string
    data = fin.read()
    print(data)
    print()

    #use a regex function to replace all end of line characters with a space
    newData = re.sub('\n',' ', data)
    print(newData)

    #Split the string at each space.  The result should be a list of words
    dataLst = newData.split()
    print (dataLst)

    #Print the number of tokens in the list.  This is not the number of words
    print(dataLst)
    
    fin.close
    
main()
