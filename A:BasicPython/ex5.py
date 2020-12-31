
from random import seed, randint

def GenNums(howMany,start,end):
    seed()
    for i in range(howMany):
        print(randint(start,end))  #start <= num <= end
        
def main():
    GenNums(10,1,100)
    
main()
