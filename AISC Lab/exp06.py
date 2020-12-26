import numpy as np
import sympy as sy
from collections import defaultdict


def FIS(indvarkeys, var, dVar, fuzzyKB):
    case = {}
    for i in indvarkeys:
        case[i] = int(input("Input Crisp Value for {} : ".format(i)))

    # Fuzzification Logic
    fuzzy = {}
    for i in indvarkeys:
        fuzzy[i] = []
        for j in var[i].keys():
            for k in range(len(var[i][j]['range'])):
                if int(var[i][j]['range'][k][0]) <= case[i] <= int(var[i][j]['range'][k][1]):
                    val = eval(var[i][j]['mem_func']
                               [k].replace('y', str(case[i])))
                    fuzzy[i].append((j, val))
    print("\nFuzzy converted Input :")
    for i in indvarkeys:
        print(i, end=" : ")
        print(fuzzy[i])

    # Fuzzy Inference Logic
    inference = defaultdict(lambda: float('-inf'))
    for i in fuzzy[indvarkeys[1]]:
        for j in fuzzy[indvarkeys[0]]:
            inference[fuzzyKB[(i[0], j[0])]] = max(
                min(i[1], j[1]), inference[fuzzyKB[(i[0], j[0])]])
    inference = dict(inference)
    print("\nFuzzy Inference for {} after min operation : {}".format(depVar, inference))

    # DeFuzzification Logic
    bestFit = max(inference, key=lambda x: inference.get(x))
    results = []
    print("now doing Defuzzification with applying max operation using {} in {} membership function".format(
        inference[bestFit], bestFit))

    z = sy.symbols('z')
    for f in dVar[bestFit]['mem_func']:
        num, den = f.split('/')

        den = int(inference[bestFit] * float(den))
        eq = num[1:-1] + '-' + str(den)
        results.append(sy.solve((eq), (z))[0])

    answer = sum(results)/len(results)
    print("\nThus {} mins that is {} time is the time taken for {} with {}.".format(
        answer, bestFit, depVar, case))
    print("------------------------------------------------------------------------------------------------")


var = {}
stop = True
numIndVar = int(input("Enter Number of independent variables >>>> "))
for i in range(numIndVar):
    indvar = input("\nEnter the independent variable name >>>> ").upper()
    var[indvar] = {}
    c = int(input("Enter Total number of Classes >>>> "))
    for i in range(c):
        cName = input("Enter the Class Name >>>> ").upper()
        cr = input("Range of the class >>>> ")
        var[indvar][cName] = {'range': [], 'mem_func': []}
        while stop:

            var[indvar][cName]['range'].append(tuple(cr.split()))
            var[indvar][cName]['mem_func'].append(
                input("Membership Function >>>> "))
            if input(f"To add more Membership Function for {cName} Press Y else press N >>>> ") not in ['y', 'Y']:
                break
            cr = input(" Range of the class >>>> ")
print("\nIndependent Variables >>>> \n", var)


depVar = input("\nEnter Dependent Variable Name >>>> ").upper()
numdepVar = int(input("Enter Total number of Classes >>>> "))
dVar = {}
stop = True
for i in range(numdepVar):
    cName = input("Enter the Class Name >>>> ").upper()
    cr = input("Range of the class >>>> ")
    dVar[cName] = {'range': [], 'mem_func': []}
    while stop:
        dVar[cName]['range'].append(tuple(cr.split()))
        dVar[cName]['mem_func'].append(input("Membership Function >>>> "))
        if input(f"To add more Membership Function for {cName} Press Y else press N >>>> ") not in ['y', 'Y']:
            break
        cr = input("Range of the class >>>> ")

print("\nDependent Variables >>>> \n", dVar)


# Construct Knowledge Base
print("\n---To construct the fuzzy Knowledge Base, create the rules---")
indvarkeys = list(var.keys())
fuzzyKB = {}
for i in var[indvarkeys[1]].keys():
    print("If {} {} >>>> ".format(indvarkeys[1], i))
    for j in var[indvarkeys[0]].keys():
        fuzzyKB[(i, j)] = input(f"\tand {indvarkeys[0]} {j} >>>> ").upper()

print("\nFuzzy KB Rules >>>> \n", fuzzyKB)

main_inp = int(input("How many times do you want to run the program ? "))
for i in range(main_inp):
    FIS(indvarkeys, var, dVar, fuzzyKB)
