import numpy

s = input("Features: ")

features = numpy.asarray(s.split(','))
print(features[0])

finishedFeatures = []
finishedFeaturesSub = []

# for i in range(len(features)):    
for j in range(len(features)):
    finishedFeaturesSub.append(features[j].split('='))
    finishedFeatures.append(finishedFeaturesSub[j])    


for i in range(len(finishedFeatures)):
    for j in range(len(finishedFeaturesSub)):
        finishedFeaturesSub[j] = [s.replace('f', '') for s in finishedFeaturesSub[j]]
        finishedFeaturesSub[j] = [s.replace(' ', '') for s in finishedFeaturesSub[j]]

features = numpy.asarray(finishedFeaturesSub).astype(int)
        

