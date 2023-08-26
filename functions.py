import numpy as np


def checkoneline(anarray):
    if len(anarray) != 9:
        return 0
    else:
        flag = 1
        for i in range(1, 10):
            if i in anarray:
                flag = flag * 1
            else:
                flag = flag * 0
        return flag


def checkfullsolution(fullarray):
    flag = 1
    for i in range(fullarray.shape[0]):
        flag = flag * checkoneline(fullarray[i])
    return flag


def arraysgenerator(mainarray):
    generated = np.zeros(shape=(27, 9))
    for i in range(9):
        generated[i] = mainarray[i]
    for i in range(9, 18):
        generated[i] = mainarray[:, i-9]
    generated[18] = np.ravel(mainarray[0:3, 0:3])
    generated[19] = np.ravel(mainarray[0:3, 3:6])
    generated[20] = np.ravel(mainarray[0:3, 6:9])
    generated[21] = np.ravel(mainarray[3:6, 0:3])
    generated[22] = np.ravel(mainarray[3:6, 3:6])
    generated[23] = np.ravel(mainarray[3:6, 6:9])
    generated[24] = np.ravel(mainarray[6:9, 0:3])
    generated[25] = np.ravel(mainarray[6:9, 3:6])
    generated[26] = np.ravel(mainarray[6:9, 6:9])
    return generated


def fillonezero(anarray):
    counter = 0
    flag = False
    for i in anarray:
        if i == 0:
            counter += 1
    if counter == 1:
        for i in range(len(anarray)):
            if anarray[i] == 0:
                anarray[i] = 45 - anarray.sum()
                print("Filled one")
                flag = True
    return flag


def fillallonezeros(fullarray):
    options = np.array([])
    flag = True
    while flag:
        flag = False
        for index, item in np.ndenumerate(fullarray):
            if item == 0:
                for i in range(1, 10):
                    if i not in fullarray[index[0]]:
                        if i not in fullarray[:, index[1]]:
                            loc = np.array(index)
                            loc = loc // 3
                            if i not in fullarray[loc[0]*3:loc[0]*3+3, loc[1]*3:loc[1]*3+3]:
                                options = np.append(options, i)
                if len(options) == 1:
                    fullarray[index] = options[0]
                    print("Filled a value")
                    flag = True

                options = np.array([])


def findoptions(fullarray):
    listofvalues = []
    for index, item in np.ndenumerate(fullarray):
        if item == 0:
            valuesofthiscell = [index]
            tupleofvalues = []
            for i in range(1, 10):
                if i not in fullarray[index[0]]:
                    if i not in fullarray[:, index[1]]:
                        loc = np.array(index)
                        loc = loc // 3
                        if i not in fullarray[loc[0] * 3:loc[0] * 3 + 3, loc[1] * 3:loc[1] * 3 + 3]:
                            tupleofvalues.append(i)
            valuesofthiscell.append(tupleofvalues)
            listofvalues.append(valuesofthiscell)
        listofvalues = sorted(listofvalues, key=lambda x: len(x[1]))
    return listofvalues

# def tryingfunc(fullarray, options):

