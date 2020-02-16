#Example 2


def f2(nameList):
    for item in nameList:
        print(item)
    for i in range (len(nameList)):
        print(nameList[i])
    
def main():
    print("How many names do you want to enter")
    num = int(input())
    nameList = []       #initialize a list. It's a lot like an array
    for i in range(num):
        print("enter a name")
        name = input()
        nameList.append(name)
    f2(nameList)

main()
