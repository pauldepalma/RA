#Example 5
#A Dictionary is a collection of key:value pairs.  The keys must be unique
#The keys and values can be either numeric or strings.
#There are lots of other things that can be done with a dictionary, but
#the example below covers the most common uses


def displayKeys(dict):
    dictKeys = (dict.keys())  #extracts the keys
    print()
    print("here are the keys, one to a line")
    for key in dictKeys:
        print(key)
    print("here are the keys as a list")
    keyList = list(dictKeys) #turn dictKeys into a list
    print(keyList)

def displayValues(dict):
    dictValues = dict.values()  #extracts the values
    print()
    print("here are the values, one to a line")
    for value in dictValues:
        print(value)
    print("here are the values as a list")
    valueList = list(dictValues) #turn dictValues into a list
    print(valueList)

def isIn(dict,name):
    if name in dict:  #returns True of the key is in dict False otherwise
        print(name + " is in the dictionary")
        print(name + "'s class is: " + dict[name]) #get the value for a name
    else:
        print(name + " is not in dictionary")
              
def whoIsHere(dict):
    print("Determine who is in the dictionary")
    name = '' #initialize a variable to the empty string
    while(name != 'Quit'):   #another looping technique. Quit if Quit is entered
        print("Enter a name or enter 'Quit' to end the program")
        name = input()
        if name != 'Quit':
            isIn(dict,name)  
    
def main():
    #This dictionary maps names to college class
    dict = {'Sami':'frosh','Angela':'Soph','Aaron':'Soph'}

    #+ concatentates strings.  len is a function that returns
    #the number of keys in dict or items in a list.
    #str transforms the int return value of len into a string
    print("We have data for " + str(len(dict)) + " students")

    #call three functions with the dictionary as the argument
    displayKeys(dict)
    print()
    displayValues(dict)
    print()
    whoIsHere(dict)

   
main()
