

# This file was *autogenerated* from the file 4-permuting.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_26 = Integer(26); _sage_const_65 = Integer(65)#Generate the alphabet
lst = [chr(i) for i in range( ord('A'), (ord('Z') + _sage_const_1  ) ) ]
lst1 = [] 
for i  in range(_sage_const_26 ):
 lst1.append(chr(i+_sage_const_65 )) 
print(lst)
print(lst1)

'''
#Permute the list using a Sage function
lstP = Permutations(lst).random_element()

#python also permutes 
import random
import copy
lstPy  = copy.deepcopy(lst) #preserve the original list
random.shuffle(lst) #permute original list
for i in range(26):
 print(lstPy[i] + ' ' + lst[i]  + ' ' )

print()
#to make it clearer, we'll permute a short sequence of integers
lst = [1,2,3,4,5]
print(Permutations(lst).random_element())
'''

