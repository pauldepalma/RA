

def evenOrOdd(num):
    if num % 2 == 0:      #modulus operator 
        return True
    return False
        
def main():
    num = 12
    if evenOrOdd(num):
       print(str(num) + " is even")
    else:
        print(str(num) + " is odd")
  
    
main()
