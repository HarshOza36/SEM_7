def computeMP(x1, x2, w1, w2, theta, y):
    ycheck = [0, 0, 0, 0]
    ynet = []
    for i in range(0, 4):
        zin = x1[i]*w1 + x2[i]*w2
        ynet.append(zin)
        if zin >= theta:
            ycheck[i] = 1
        else:
            ycheck[i] = 0
    for i in range(0, 4):
        if ycheck[i] != y[i]:
            return False
    print(f'Weights Trained >>> {w1} , {w2}')
    print('Threshold >>> ', theta)
    print('Y >>> ', ycheck)
    print('Y-Net >>> ', ynet)
    return True


def computeMP_NOT(x, w, theta, y):
    ycheck = [0, 0]
    ynet = []
    for i in range(0, 2):
        zin = x[i]*w
        ynet.append(zin)
        if zin >= theta:
            ycheck[i] = 1
        else:
            ycheck[i] = 0
    for i in range(0, 2):
        if ycheck[i] != y[i]:
            return False
    print(f'Weights Trained >>> {w}')
    print('Threshold >>> ', theta)
    print('Y >>> ', ycheck)
    print('Y-Net >>> ', ynet)
    return True


def andLogic(weights, threshold_values):
    AND = [0, 0, 0, 1]
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    for w1 in weights:
        for w2 in weights:
            for theta in threshold_values:
                stop = computeMP(x1, x2, w1, w2, theta, AND)
                if stop:
                    break
            if stop:
                break
        if stop:
            break


def orLogic(weights, threshold_values):
    OR = [0, 1, 1, 1]
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    for w1 in weights:
        for w2 in weights:
            for theta in threshold_values:
                stop = computeMP(x1, x2, w1, w2, theta, OR)
                if stop:
                    break
            if stop:
                break
        if stop:
            break


def nandLogic(weights, threshold_values):
    NAND = [1, 1, 1, 0]
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    for w1 in weights:
        for w2 in weights:
            for theta in threshold_values:
                stop = computeMP(x1, x2, w1, w2, theta, NAND)
                if stop:
                    break
            if stop:
                break
        if stop:
            break


def norLogic(weights, threshold_values):
    NOR = [1, 0, 0, 0]
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    for w1 in weights:
        for w2 in weights:
            for theta in threshold_values:
                stop = computeMP(x1, x2, w1, w2, theta, NOR)
                if stop:
                    break
            if stop:
                break
        if stop:
            break


def notLogic(weights, threshold_values):
    NOT = [1, 0]
    x = [0, 1]
    for w in weights:
        for theta in threshold_values:
            stop = computeMP_NOT(x, w, theta, NOT)
            if stop:
                break
        if stop:
            break


weights = [1, -1]
threshold_values = [-1, 0, 1, 2]
print("<<<< MP Model - AND Gate >>>>>")
andLogic(weights, threshold_values)
print("\n<<<< MP Model - OR Gate >>>>>")
orLogic(weights, threshold_values)
print("\n<<<< MP Model - NAND Gate >>>>>")
nandLogic(weights, threshold_values)
print("\n<<<< MP Model - NOR Gate >>>>>")
norLogic(weights, threshold_values)
print("\n<<<< MP Model - NOT Gate >>>>>")
notLogic(weights, threshold_values)
