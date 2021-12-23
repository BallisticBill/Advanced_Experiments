import numpy as np
import matplotlib.pyplot as plt
import random as rnd

def atomic_decay(N, decay_const, time_lim):
    t=0
    res = []
    while(t<=time_lim):
        mean = N*decay_const*0.001
        n_delta = np.random.poisson(lam=mean,size=1)[0]
        N = N - n_delta
        res.append(N)
        t += 0.001
    return res

def decay_alt(N,decay_const,time_lim): #additional exercise
    t=0
    delta_t = 0.001
    res=[N]
    while(t<time_lim and N >= 0):
        ln = N
        for i  in range(ln):
            if rnd.random() < decay_const*delta_t:
                N -= 1
        res.append(N)
        t += delta_t
    return res


y_final = [0 for i in range(5000)]

for i in range(100):
    temp = atomic_decay(1000,0.6,5)
    for j in range(len(temp)):
        y_final[j] = y_final[j]+temp[j]/100

plt.title(r'Radioactive Decay of 1000 atoms in 5 seconds ($\lambda$ = 0.6)',fontsize=15)
plt.xlabel("time t",fontsize=12)
plt.ylabel('Number of atoms remaining N(t)',fontsize=12)
plt.plot(np.linspace(0,5,len(y_final)),y_final)
plt.plot((x:=np.linspace(0,5,100)),100+1000*np.exp(-0.6*x),'r')
plt.legend(['simulated value','theoretical value'])
plt.show()

y_final = [0 for i in range(1001)]

for i in range(100):
    temp = decay_alt(1000,0.6,1)
    for j in range(len(temp)):
        y_final[j] = y_final[j]+temp[j]/100

plt.title(r'Radioactive Decay of 1000 atoms in 1 second (Additional Excercise) ($\lambda$ = 6)',fontsize=15)
plt.xlabel("time t",fontsize=12)
plt.ylabel('Number of atoms remaining N(t)',fontsize=12)
plt.plot(np.linspace(0,5,len(y_final)),y_final)
plt.plot((x:=np.linspace(0,5,100)),1000*np.exp(-0.6*x),'r')
plt.legend(['simulated value','theoretical value'])
plt.show()

