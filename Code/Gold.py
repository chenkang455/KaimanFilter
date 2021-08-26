#
import matplotlib.pyplot as plt
import random
value=100 #设定金条的质量
nums=100 #设定称重的次数
values=[]
alpha=0 #卡尔曼增益
for i in range(100):
    values.append(value+random.gauss(0,3))
optimal_value=90 #一开始的最优估计随机选取
optimal_values=[90]
for N in range(100):
    alpha=1/(N+1)
    optimal_value+= alpha*(values[N]-optimal_value)
    optimal_values.append(optimal_value)
plt.plot(values,label='Measurement')
plt.plot(optimal_values,label='OptimalEstimate')
plt.legend()
plt.show()