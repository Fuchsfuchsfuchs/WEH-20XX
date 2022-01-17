import math
import numpy as np
from typing import List, Set, Dict, Tuple, Optional

class MalePop:
    impregnationsPerDay: List[int] = [3,3,3,3,3,3,3]
    age: List[int] = [20,23,25,22,27,30,45]

class FemalePop:
    pregnant: List[int] = [0] * 10
    age: List[int] = []

import pandas as pd
csvPops = pd.read_csv("WORLD-2040.csv")
(csvPopsAge,csvPopsFemale) = (csvPops["Age"],csvPops["F"])

def initWomans(csvPopsAge,csvPopsFemale):
    femalePop: FemalePop = FemalePop()
    for i in range(len(csvPopsAge)):
        ages = csvPopsAge[i].split("-")
        ages[0] = int(ages[0])
        ages[1] = int(ages[1])
        num = int(csvPopsFemale[i])
        numAges = ages[1] - ages[0] + 1
        numPerAge  = int(num/numAges)
        print(numPerAge)
        for ageI in range(numAges):
            age = ages[0] + ageI
            femalePop.age.append([age]*numPerAge)
            femalePop.pregnant.append([0]*numPerAge)

malePop: MalePop = MalePop()
femalePop: FemalePop  = initWomans(csvPopsAge,csvPopsFemale)
reproductionStartAge = 18
#{pregnant: [0,100], age: [20,30]}

def getHornyFemale(femalePop: FemalePop, num: int )->List[int]:
    hornyFemales = []
    for i in range(len(femalePop.age)):
        if (len(hornyFemales) == num): break
        if femalePop.age[i] > reproductionStartAge and femalePop.pregnant[i]:
            hornyFemales.append(i)
    return hornyFemales

def updatePregnancies(femalePop: FemalePop):
    for i in range(len(femalePop.age)):
        if(femalePop.pregnant[i]):
            femalePop.pregnant[i] += 1

def killHumans(malePop: MalePop,femalePop: FemalePop):
    toKill = []
    for i in range(len(malePop.age)):
        if malePop.age[i] > 100:
            toKill.append(i)
    for k in toKill:
        malePop.age.pop(k)
        malePop.impregnationsPerDay.pop(k)
    toKill = []
    for i in range(len(femalePop.age)):
        if femalePop.age[i] > 100:
            toKill.append(i)
    for k in toKill:
        femalePop.age.pop(k)
        femalePop.impregnationsPerDay.pop(k)


def update(malePop: MalePop,femalePop: FemalePop, waitingTime = 4 * 365):

    for i in range(len(malePop.age)):
        if malePop.age[i] > reproductionStartAge:
            hornyFemales = getHornyFemale(femalePop,malePop.impregnationsPerDay[i])
            for female in hornyFemales:
                femalePop.pregnant[i] = 1
    
    updatePregnancies(femalePop)
    killHumans(malePop,femalePop)
    
