#Characters preceded by # forms a comment
'''
Three apostrophes
followed by three apostrophes
form a multi-line comment
'''

#The following line brings in the python math library.
import math


def main():

    #To align on the decimal, precision must be the same
    print("{:12.2f}".format(99.78))         #width 12, precision 2
    print("{:12.2f}".format(math.pi))       #width 12, precision 2
    print("{:12.4f}".format(112345.16778))  #width 12, precision 4

    #the above three strings as variables padded with zeroes 
    num1 = "{:012.2f}".format(99.78)
    num2 = "{:012.2f}".format(math.pi)      
    num3 = "{:012.4f}".format(112345.16778)
    print (num1)
    print (num2)
    print (num3)
    
main()
