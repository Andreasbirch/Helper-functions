import numpy

s = input("Features: ")

features = numpy.asarray(s.split(','))
print(features[0])

finishedFeatures = []
for i in range(len(features)):
    finishedFeatures.append(features[i].split('='))
    features[i] = str(features[i]).split('=')

