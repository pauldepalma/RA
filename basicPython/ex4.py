#Example 4

    
def main():
    fin = open("ex4.txt", 'r')
    fout = open("ex4.txtOut",'w')
    for line in fin:
        fout.write(line)
    fin.close()
    fout.close()
    
main()
