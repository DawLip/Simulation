from random import randrange
from time import process_time

# possibilities = [1,1,1,1,1,1, 2,2,2, 3]
result = {
    "(0, 0, 0)": 0,
    "(1, 1, 1)": 0,
    "(2, 2, 100)": 0,
}
result2 = {
    "(0, 0)": 0,
    "(1, 1)": 0,
    "(2, 2)": 0,
}

freeSpaces = [(0,0,0),(1,1,1),(2,2,100)]
maxDistance = max([space[2] for space in freeSpaces])+1

# start=process_time()
# for _ in range(1_000_000):
#     probabilitySpaces = []
#     for space in freeSpaces:
#         s=[(space[0],space[1]) for i in range(maxDistance//(space[2]+1))]
#         probabilitySpaces.extend(s)

#     selectedSpace = probabilitySpaces[randrange(len(probabilitySpaces))]
#     result2[f'{selectedSpace}']+=1
# stop=process_time()
# print(stop-start)
    
start=process_time()
for _ in range(1_000_000):
    probabilitySpaces = []
    sumOfProbability=0
    for space in freeSpaces:
        probability=maxDistance//(space[2]+1)
        sumOfProbability+=probability
        probabilitySpaces.append(sumOfProbability)
        
    selectedSpace = freeSpaces[0]
    for index,p in enumerate(probabilitySpaces):
        if p > randrange(sumOfProbability+1):
            selectedSpace=freeSpaces[index]
            break
    
    result[f'{selectedSpace}']+=1
    
stop=process_time()
print(stop-start) 

# print(result2)
print(result)