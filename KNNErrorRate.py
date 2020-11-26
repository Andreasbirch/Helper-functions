import numpy
import sys

rawTextInput = input("Paste ENTIRE Table here: ")
trueClassesText = input("Type the groups as a list with indices separated by spaces. Do not use brackets: ")
K = input("Type K, for nearest neighbour calculation: ")
K = int(K)

wrongCounter = 0
rightCounter = 0


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

##Setup class grouping
trueClasses = numpy.asarray(trueClassesText.split())
noOfDifferentClasses = 1
entryClass = trueClasses[0]
trueClassRanges = numpy.empty(noOfDifferentClasses)
trueClassRanges[0] = [1,2,3]
sys.exit()

##Done reading data
for i in range(noOfDifferentClasses):
    for j in range(1,len(trueClasses)):
        if(trueClasses[j] != entryClass):
            noOfDifferentClasses += 1
            trueClassRanges[i] = [entryClass, j]
            entryClass = trueClasses[j]
    


##Calculate
## Density of nearest neighbours
def KNN(list, K):
    KNNIndices = numpy.argsort(list)[1:K+1]
    KNNValues = numpy.empty(K)
    for i in range(K):
        KNNValues[i] = list[KNNIndices[i]]
    return numpy.asarray([KNNIndices,KNNValues])


##Run KNN with crossvalidation
# for i in range(len(rownames)):
#     neighbours = KNN(data[i], K)
#     for j in range(len(neighbours)):
#         # if(neighbours[0][j] != )
#     print()
    