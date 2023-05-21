import time
import random
from numba import jit


randomNum = 10
start = time.process_time()
# @jit(nopython=True)
def foo():
    res=[]
    for _ in range(500_000):
        stemCells = [(0,1),(0,0),(1,0),(1,2),(4,5),(2,4),(4,5),(8,4),(2,1),(3,6),(0,1),(0,0),(1,0),(1,2),(4,5),(2,4),(4,5),(8,4),(2,1),(3,6),(0,1),(0,0),(1,0),(1,2),(4,5),(2,4),(4,5),(8,4),(2,1),(3,6)]
        freeSpaces = set()
        for stem in stemCells:
            # if stem[0] != 0 :
                freeSpaces.add((stem[0]-1, stem[1]))
            # if stem[1] != 0 :
                freeSpaces.add((stem[0], stem[1]-1))
            # if stem[0] != 100:
                freeSpaces.add((stem[0]+1, stem[1]))
            # if stem[1] != 100:
                freeSpaces.add((stem[0], stem[1]+1))
        res.append(list(freeSpaces)[randomNum])
    return(res)    
res=foo()
stop = time.process_time()
print(stop - start)
print(len(res))


      