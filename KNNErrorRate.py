import numpy
import sys

rawTextInput = input("Paste ENTIRE Table here: ")
trueClassesText = input("Type the last index oi of each group (you dont have to include the first or last index), separated by spaces \nFor example 2 6 8 10: ")


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
trueClasses = trueClasses.astype(int)
if(trueClasses[-1] != len(colnames)):
    trueClasses = numpy.append(trueClasses, len(colnames))

if(trueClasses[0] != 1 or trueClasses[0] != 0):
    trueClasses = numpy.append(0, trueClasses)


##Create list of classes
classCounter = 1
classes = []

for i in range(len(trueClasses)):
    try:
        for j in range(trueClasses[i], trueClasses[i+1]):
            classes.append(classCounter)
        classCounter += 1
    except(IndexError):
        break
   
print("interpreted input as following groups: ", classes)
K = input("Type K, for nearest neighbour calculation: ")
K = int(K)
    
##Calculate
## Density of nearest neighbours
def KNN(list, K):
    KNNIndices = numpy.argsort(list)[1:K+1]
    KNNValues = numpy.empty(K)
    for i in range(K):
        KNNValues[i] = list[KNNIndices[i]]
    return numpy.asarray([KNNIndices,KNNValues])


def ContainsRepeats(list):
    for i in range(len(list)):
        try:
            for j in range(i+1, len(list)):
                if(list[i] == list[j]):
                    return True
        except:
            print()
    return False


def DetermineClass(list):
    if(ContainsRepeats(list)):    
        noOfOccurences = 0
        mostOccuringClass = 0
        for i in range(len(list)):
            counter = 0
            try:
                for j in range(i+1, len(list)):
                    if(list[i] == list[j]):
                        counter += 1
            except:
                print()
            if(counter > noOfOccurences):
                noOfOccurences = counter
                mostOccuringClass = list[i]
            
        return [mostOccuringClass, noOfOccurences]


for i in range(len(rownames)):
    neighbours = KNN(data[i],K)
    neighbourClasses = numpy.empty(len(neighbours[0]))
    for j in range(len(neighbourClasses)):
        neighbourClasses[j] = classes[int(neighbours[0][j])]
        
    if(ContainsRepeats(neighbourClasses) == False):
        if(classes[i] != classes[int(neighbours[0][0])]):
            wrongCounter += 1
        else:
            rightCounter += 1
    else:
        if(classes[i] != int(DetermineClass(neighbourClasses)[0])):
            wrongCounter += 1
        else:
            rightCounter += 1
    print()

print("Error rate: ", wrongCounter, "/", (wrongCounter + rightCounter))
print("Succes rate: ", rightCounter, "/", (wrongCounter + rightCounter))
    