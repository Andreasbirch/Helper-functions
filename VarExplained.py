import numpy
import sys

matrixSInput = input("Paste matrix S \nCaution, do not copy the vertical bars of the matrices: ")
pCInput = input("Type the indicises of the components you need variance explained for, separated with space.\nFor example, for the first two components you would write 1 2\n")

pC = numpy.asarray(pCInput.split()).astype(int) - 1

##Read data, setup
#Matrix
npArr = numpy.asarray([i.split() for i in matrixSInput.split('\n')])
if(len(npArr[0])==0):
    npArr = npArr[1:]
npArr = numpy.char.replace(npArr,'−','-')
npArr = numpy.char.replace(npArr,':','.')
S = npArr.astype(float)

sumOfPC = 0
for i in range(len(pC)):
    sumOfPC = sumOfPC + S[pC[i]][pC[i]]**2
    
sumOfAll = 0
for i in range(len(S[0])):
    sumOfAll = sumOfAll + S[i][i]**2
    
print("Variance explained by indices: ", pC + 1, " is", sumOfPC/sumOfAll, " or ", int((sumOfPC/sumOfAll)*100),"%")