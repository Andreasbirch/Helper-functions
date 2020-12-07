# -*- coding: utf-8 -*-
import numpy
import sys

rawTextInput = input("Paste ENTIRE Table here: ")
target = input("Type the number of row or column that needs to be searched: ")
K = input("Type K, for nearest neighbour calculation: ")

target = target.replace('O', '')
target = target.replace('o', '')
target = target.replace(' ', '')
target = int(target) - 1
K = int(K)

##Read data, setup
npArr = numpy.asarray([i.split() for i in rawTextInput.split('\n')])
if(len(npArr[0])==0):
    npArr = npArr[1:]
    
colnames = npArr[0][:]
rownames = npArr[:][0]

data = numpy.empty((len(colnames),len(rownames)))
for i in range(1,len(colnames)):
    for j in range(1,len(colnames)):
        data[i-1][j-1] = npArr[i][j]
    data[i-1][len(colnames)-1] = npArr[i][len(colnames)]
    
data[len(colnames)-1][:] = npArr[len(colnames)][1:]

##Calculate
## Density of nearest neighbours
def KNN(list, K):
    KNNIndices = numpy.argsort(list)[1:K+1]
    KNNValues = numpy.empty(K)
    for i in range(K):
        KNNValues[i] = list[KNNIndices[i]]
    return numpy.asarray([KNNIndices,KNNValues])

def LocalDensity(list):
    localSum = 0
    for i in range(len(list)):
        try:
            localSum = localSum + list[1][i]
        except(IndexError):
            return list[1][0]
    return localSum

targetKNN = KNN(data[target], K)

##Calclate densities
sum = 0;
subDensities = numpy.empty(K)

for j in range(len(targetKNN[0])):
    subKNN = KNN(data[int(targetKNN[0][j])],K)
    subSum = 0
    subDensities[j] = 1/(1/K*(LocalDensity(subKNN)))

subDensitiesSum = 0
for i in subDensities:
    subDensitiesSum = subDensitiesSum + i


##Calculate ARD
print("Nearest neighbours of o", str(target + 1), " is ", targetKNN[0]+1 )
print("ARD: ", 1/(1/K*(LocalDensity(targetKNN)))/(1/K*(subDensitiesSum)))