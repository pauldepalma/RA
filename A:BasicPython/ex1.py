#This is a python comment
#Example 1

'''
This is a multi-line comment
There are types in python, but their context defines them
The variable, value, below is a string.
I turn it into an int to iterate over it
'''



#This is a python function
def f1(valueIn):
    for i in range(valueIn):   #This is a python loop
        print(i)
        print("Welcome to Python")


def main():
    print ("Enter an integer")
    value = int(input())    #This gets input from the keyboard
    f1(value)   #This invokes a function

main()
