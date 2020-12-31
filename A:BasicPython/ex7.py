

def evenOrOdd(num):
    if num % 2 == 0:      #modulus operator 
        return True
    return False
        
def main():
    while (True):
        print("Enter an integer")
        num = int(input())
        if evenOrOdd(num):
           print(str(num) + " is even")
        else:
            print(str(num) + " is odd")
        print("Enter Another (y/n)")
        more = input()
        if more == 'n':
              break
              
  
    
main()
