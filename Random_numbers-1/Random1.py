import random as rnd 
import matplotlib.pyplot as plt 
import numpy as np
import math

def quantum(size):
    res=[]
    while(len(res)<size):
        y = 2*rnd.random()
        x = rnd.random()
        if y < (2*math.sin(math.pi*x)**2):
            res.append(x)
    return res


def generate_gaussian(length):
    res=[]
    for i in range(length):
        res.append(rnd.gauss(0,1))
    return res

def histogram(x,y,title):
    fig,ax = plt.subplots(1,1)
    ax.text(0, 40000, r'$\mu=0,\ \sigma=1$')
    plt.plot((x:=np.linspace(-3,3,100)),[1/np.sqrt(2*np.pi)*math.exp(-i**2 / 2) for i in x])
    plt.hist(y,bins=x,density=True)
    plt.title(title)
    plt.xlabel('Random Variable X',fontsize=11)
    plt.ylabel('Probabiliy Density P(X)',fontsize=11)
    plt.show()



def main():

    arr = [10*rnd.random() for i in range(1000000)]
    plt.title("1000000 Uniform Random Numbers Between 0 and 10",fontsize=12)
    plt.hist(arr,100,density=True)
    plt.xlabel("Random variable X",fontsize=11)
    plt.ylabel("Probability density P(X)",fontsize=11)
    plt.show()

    arr = [10*rnd.random() for i in range(10000)]
    plt.title("10000 Uniform Random Numbers Between 0 and 10",fontsize=12)
    plt.hist(arr,40,density=True)
    plt.xlabel("Random variable X",fontsize=11)
    plt.ylabel("Probability density P(X)",fontsize=11)
    plt.show()

    arr = [10*rnd.random() for i in range(1000)]
    plt.title("1000 Uniform Random Numbers Between 0 and 10",fontsize=12)
    plt.hist(arr,10,density=True)
    plt.xlabel("Random variable X",fontsize=11)
    plt.ylabel("Probability density P(X)",fontsize=11)
    plt.show()
    val=generate_gaussian(3000000)
    histogram(np.linspace(-3,3,100),val,"Gaussian Distribution of 3000000 Numbers")
    val=generate_gaussian(30000)
    histogram(np.linspace(-3,3,100),val,"Gaussian Distribution of 30000 Numbers")
    val=generate_gaussian(3000)
    histogram(np.linspace(-3,3,100),val,"Gaussian Distribution of 3000 Numbers")
    x = quantum(10000)
    plt.title('Particle in a box')
    plt.hist(x,100,density=True)
    plt.plot((arr:=np.linspace(0,1,100)),[2*math.sin(math.pi*x)**2 for x in arr])
    plt.xlabel("Random variable X",fontsize=11)
    plt.ylabel(r'$\psi (X)$',fontsize=14)
    plt.show()


if __name__=="__main__":
    main()
