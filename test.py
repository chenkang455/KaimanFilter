import matplotlib.pyplot as plt
import random
import numpy as np

data = np.loadtxt("testdata.txt", delimiter=' ', dtype=np.float32)
values=data[:,-1]
mean=np.mean(values)
std=np.std(values)



#Set the basic value
value=300
#Model the gauss noise with the standard deviation
# values=[]
# for i in range(100):
    # values.append(value+random.gauss(0,10))

#Parameters
p=25
K=0
#Measurement uncertainty
r=1
#First Estimate 
estimate=100
estimates=[]
KS=[]
for i in range(len(values)):
    K=p/(p+r)
    measure=values[i]
    #Predcit
    estimate = estimate+K*(measure-estimate)
    estimates.append(estimate)
    p=(1-K)*p
    KS.append(K)
plt.plot(values)
plt.plot(estimates)
print(estimate)
plt.show()
