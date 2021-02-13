#Illustrates simple matplotlib plot
#first install pip from the command line
# sudo apt-get install -y python3-pip
#now install matplotlib from the command line
#pip install matplotlib


import matplotlib.pyplot as plt


def main():
    x = [i for i in range(-100,100)]
    y = [i*i for i in x] 
    plt.plot(x,y)
    plt.show()
    
main()
    
