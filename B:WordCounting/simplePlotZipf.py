

import matplotlib.pyplot as plt

import math


def plot_zipf(x,y,xx,yy):

    plt.plot(x,y) #classic zipf plot
    #plt.plot(xx,yy) #log-log plot
        
    plt.show()
        
   
def main():

        x = [i for i in range (1,11)]
        y = [1/i for i in x]
        xx = [math.log(i) for i in x]
        yy = [math.log(i) for i in y]
        plot_zipf(x,y,xx,yy)
    
    
    
main()
