import random
from time import time
n=10000000
i=0
start_time =time()
for _ in range(n):
    x= random.uniform(-1,1)
    y= random.uniform(-1,1)
    r= x**2 + y**2
    # print(f'x:{x}, y:{y}, r: {r} ')
    if (x**2+y**2) <=1:
        i+=1
pi = 4 * i/n
end_time = time()
print('pi: %10.5f, i:%10d, n: %10d '%(pi,i,n))
print('The elapsed time:%.5f' %(end_time-start_time))