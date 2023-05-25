l1=[14,40,31,28,3,15,17,51]
l2=[1,2,3,4,5,6]
l3=[6,5,4,3,2,1]
l4=[2,2,2,2,2,2,2]

def minF(l):
    if len(l) == 1:     return l[0]
    if len(l) == 2:
        if l[0] < l[1]: return l[0]
        return l[1]
    else: 
        if minF(l[:len(l)//2]) < minF(l[len(l)//2:]):
            return minF(l[:len(l)//2])
        return minF(l[len(l)//2:])


print(minF(l1))
print(minF(l2))
print(minF(l3))
print(minF(l4))
# from random import randrange

# data = {
#     'simWidth':100,
#     'simHeight':100,
# }

# possibleSpaces = [(-1,1),(0,1000),(1,0),(1,2),(4,5),(2,4),(4,5),(8,4),(2,1),(3,6),(0,1),(0,0),(1,0),(1,2),(4,5),(2,4),(4,5),(8,4),(2,1),(3,6),(0,1),(0,0),(1,0),(1,2),(4,5),(2,4),(4,5),(8,4),(2,1),(3,6)]
# freeSpaces = [
#             (x, y) for x, y in possibleSpaces 
#             if x >= 0 and y >= 0 and 
#             x <= data['simWidth'] and y <= data['simHeight'] #and 
#             # data['CollisionMap'].isOccupied(x, y)
#         ]
# selectedSpace = freeSpaces[randrange(len(freeSpaces))]
# print(selectedSpace)
# from tmp.test2 import test2
# from tmp.test3 import test3

# test2()
# print(test3())

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