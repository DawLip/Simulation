from random import randrange

def calcProbability(baseProbability: list):
    if not isinstance(baseProbability, (list, tuple)):
        raise TypeError("baseProbability should be a list or tuple.")
    
    maxProbability = max(baseProbability)+1
    sumOfProbability = 0
    probability = []

    for item in baseProbability:
        itemProbability = maxProbability//(item+1)
        sumOfProbability += itemProbability
        probability.append(sumOfProbability)
    return probability

def randomChoose(data: list, probability: list or tuple):
    if not isinstance(data, (list, tuple)) or not isinstance(probability, (list, tuple)):
        raise TypeError("data and probability should be a list or tuple.")
    if len(data) != len(probability):
        raise Exception('Wrong data.')
    
    sumOfProbability = sum(probability)
    randomNum = randrange(sumOfProbability+1)
    for index, itemProbability in enumerate(probability):
        if itemProbability > randomNum:
            return data[index]