import numpy
import sys

# rawTextInput = input("Paste ENTIRE Table here: ")
# trueClassesText = input("Type the last index oi of each group (you dont have to include the first or last index), separated by spaces \nFor example 2 6 8 10: ")


# ##Read data, setup
# npArr = numpy.asarray([i.split() for i in rawTextInput.split('\n')])
# if(len(npArr[0])==0):
#     npArr = npArr[1:]
    
# colnames = npArr[0][:]
# rownames = []
# for i in range(1,len(npArr)):
#     rownames.append(npArr[i][0])
    

# data = numpy.empty((len(rownames),len(colnames)))
# for i in range(1,len(rownames)):
#     for j in range(1,len(colnames)):
#         data[i-1][j-1] = npArr[i][j]
#     data[i-1][len(colnames)-1] = npArr[i][len(colnames)]
    
# data[len(rownames)-1][:] = npArr[len(rownames)][1:]

# ##Setup class grouping
# trueClasses = numpy.asarray(trueClassesText.split())
# trueClasses = trueClasses.astype(int)
# if(trueClasses[-1] != len(colnames)):
#     trueClasses = numpy.append(trueClasses, len(colnames))

# if(trueClasses[0] != 1 or trueClasses[0] != 0):
#     trueClasses = numpy.append(0, trueClasses)

# ##Create list of classes
# classCounter = 1
# classes = []

# for i in range(len(trueClasses)):
#     try:
#         for j in range(trueClasses[i], trueClasses[i+1]):
#             classes.append(classCounter)
#         classCounter += 1
#     except(IndexError):
#         break
   
# print("interpreted input as following groups: ", classes)
# # print(trueClasses[0]-1)

# featuresString = input("Paste features: ")
# alpha = input("alpha: ")
# y = input("y: ")

# # ##Setup features list
# features = numpy.asarray(featuresString.split(','))

# finishedFeatures = []
# finishedFeaturesSub = []

# # for i in range(len(features)):    
# for j in range(len(features)):
#     finishedFeaturesSub.append(features[j].split('='))
#     finishedFeatures.append(finishedFeaturesSub[j])    


# for i in range(len(finishedFeatures)):
#     for j in range(len(finishedFeaturesSub)):
#         finishedFeaturesSub[j] = [s.replace('f', '') for s in finishedFeaturesSub[j]]
#         finishedFeaturesSub[j] = [s.replace(' ', '') for s in finishedFeaturesSub[j]]

# features = numpy.asarray(finishedFeaturesSub).astype(int)
# for i in features[0]:
#     i-= 1
# ##Done setting data





####TESTING ONLY####
## Spring 2019
data = numpy.asarray([[0,	0,	0,	1,	0,	0,	0,	0,	0], 
                      [0,	0,	0,	0,	0,	0,	0,	0,	1],
                      [0,	1,	1,	1,	1,	1,	0,	0,	0],
                      [1,	0,	0,	0,	0,	0,	0,	0,	0],
                      [1,	0,	0,	1,	0,	0,	0,	0,	0],
                      [0,	0,	1,	1,	0,	0,	0,	1,	0],
                      [0,	0,	1,	1,	1,	0,	0,	0,	0],
                      [0,	0,	0,	0,	1,	0,	0,	0,	0],
                      [0,	1,	1,	0,	1,	0,	0,	0,	0],
                      [0,	0,	1,	1,	1,	0,	1,	0,	0]])
trueClasses = numpy.asarray([0, 2, 5, 10])
classes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
features = numpy.asarray([[2, 0], [4, 1], [5, 0]])
y = 2






##Generate list to calculate hits:
def ListGenerator(column, interval):
    listout = []
    for i in range(interval[0],interval[1]+1):
        listout.append(data[i][column-1])
    return listout

def DetermineCorrectHits(ls, val):
    counter = 0
    for i in range(len(ls)):
        if(ls[i] == val):
            counter += 1
    return counter

##Calculate Naive bayes
numerator = 1
numList = []
for i in range(len(features)):
    generatedList = ListGenerator(features[i][0], [trueClasses[y-1], trueClasses[y]-1])
    correctHits = DetermineCorrectHits(generatedList, features[i][1])
    print(correctHits, "/", len(generatedList))
    numerator = numerator * correctHits/len(generatedList)
##Trueclasses[-1] bør nok ændres til len(rownames)
numerator = numerator * (classes.count(y)/trueClasses[-1])
print(classes.count(y), "/", trueClasses[-1])
print("\n")

denominator = 1
for j in range(1,len(features)+1):
    subNumerator = 1
    for i in range(len(features)):
        generatedList = ListGenerator(features[i][0], [trueClasses[j-1], trueClasses[j]-1])
        correctHits = DetermineCorrectHits(generatedList, features[i][1])
        print(correctHits, "/", len(generatedList))
        subNumerator = subNumerator * correctHits/len(generatedList)
    ##Trueclasses[-1] bør nok ændres til len(rownames)
    subNumerator = subNumerator * (classes.count(j)/trueClasses[-1])
    print(classes.count(j), "/", trueClasses[-1])
    print()
    denominator = denominator + subNumerator
denominator = denominator - 1


##Generate final result:
print(numerator / denominator)
