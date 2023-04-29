import random
import time

from test2 import test2

test2()

arr=[]
start1=time.perf_counter_ns()
for i in range(10000):
    arr.append(random.randrange(100))
stop1=time.perf_counter_ns()

arr=[]
start2=time.perf_counter_ns()
for i in range(10000):
    arr.append(random.randint(0,100))
stop2=time.perf_counter_ns()
    
print(stop1-start1,stop2-start2)