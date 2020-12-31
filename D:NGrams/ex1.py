'''
Example 9
Tuples and list comprehensions
tuples are immutable lists.  Any list function that does not change the list
itself works for a tuple.
You might find them useful in specifying grams
'''

def main():
    t0 = ('Higgledy Piggledy')
    t1 = ('Piggledy my')
    t2 = ('my black')
    lst0 = [t0,t1,t2]

    #this is a list comprehension.  list comprehensions are considered very
    #pythonic
    lst1 = [item for item in lst0]
    print(lst0)
    print(lst1)

    #Guess what this displays
    print(lst1[1][0]) 

    #now try
    #What's going on?
    t3 = ('black hen', 'hen she')
    lst1.append(t3)
    print(lst1)
    print(lst1[3][1])
    
main()
