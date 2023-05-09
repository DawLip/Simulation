from tmp.test2 import test2
from tmp.test3 import test3

test2()
print(test3())

# import time 
# from numba import jit

# def fun1():
#     a=0
#     b=1
#     c=0
#     while a<100_000_000:
#         a=a+b
#         a=a-(b*2)
#         a=a+(b*2)
#         c=a


# @jit(nopython=True)
# def fun2():
#     a=0
#     print('start')
#     while a<10000000000:
#         a=a+1
#     print(a)

# # start = time.process_time()
# # fun1()
# # end = time.process_time()

# start2 = time.process_time()
# fun2()
# end2 = time.process_time()

# # print(end-start)
# print(end2-start2)