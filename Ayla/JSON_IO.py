import json

def W_JSON(lst,fname):
  
  #transform input to serialized list
  with open(fname, "w") as f:
    json.dump(lst, f, indent=4)

def R_JSON(fname):
  with open(fname, "r") as f:
    listIn = json.load(f)
  return(listIn)

	

def main():
  fname = "list1.json"
  lst = [i for i in range(10)]
  print(lst)
  print()
  
  W_JSON(lst,fname)
  lstIn = R_JSON(fname)
  print(lstIn)
  
main()