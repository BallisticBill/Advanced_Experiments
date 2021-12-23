import matplotlib.pyplot as plt
import random as rnd

def generate_mock(func,rng,err):
    a, b, num = rng
    x, y, error = ([],[],[])
    temp = [i*(b-a)/num for i in range(num)]
    for i in temp:
        y.append((v:=func(i)) + (tmp:=rnd.gauss(0,err*v)))
        error.append(tmp)
        x.append(i)
    return x, y, error
x, y, error = generate_mock(lambda x: x**(1.5), (0,1,20), 0.05)
plt.title('Mock Data Resembling The Function Y = X$^{3/2}$',fontsize=15)
plt.xlabel('X',fontsize=12)
plt.ylabel('Y = X$^{3/2}$',fontsize=12)
plt.plot(x,y ,'o')
plt.errorbar(x,y, yerr = error,label='error in y',fmt='x')
plt.legend(['data point','error bar'])
plt.show()