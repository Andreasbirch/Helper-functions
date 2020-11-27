import numpy
import sys

rawTextInput = input("Paste ENTIRE Table here: ")
trueClassesText = input("Type the last index oi of each group (you dont have to include the first or last index), separated by spaces \nFor example 2 6 8 10: ")
testers = input("Input det der tingting: ")
alpha = input("alpha: ")
yb = input("yb: ")


##Read data, setup
npArr = numpy.asarray([i.split() for i in rawTextInput.split('\n')])
if(len(npArr[0])==0):
    npArr = npArr[1:]
    
colnames = npArr[0][:]
rownames = []
for i in range(1,len(npArr)):
    rownames.append(npArr[i][0])
    

data = numpy.empty((len(rownames),len(colnames)))
for i in range(1,len(rownames)):
    for j in range(1,len(colnames)):
        data[i-1][j-1] = npArr[i][j]
    data[i-1][len(colnames)-1] = npArr[i][len(colnames)]
    
data[len(rownames)-1][:] = npArr[len(rownames)][1:]

##Setup class grouping
trueClasses = numpy.asarray(trueClassesText.split())
trueClasses = trueClasses.astype(int)
if(trueClasses[-1] != len(rownames)):
    trueClasses = numpy.append(trueClasses, len(rownames))

if(trueClasses[0] != 1 or trueClasses[0] != 0):
    trueClasses = numpy.insert(trueClasses, 0, 0)


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

