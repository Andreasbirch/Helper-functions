import numpy
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import scipy.spatial.distance as ssd

print("CAUTION: program plots both maximum and minimum linkage. Be weary of the problem type")
rawTextInput = input("Paste ENTIRE Table here: ")
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


# For test
# data =  numpy.asarray(
#        [[0,	    0.534,	1.257,	1.671,	1.09,	1.315,	1.484,	1.253,	1.418],
#         [0.534,	0,	    0.727,	2.119,	1.526,	1.689,	1.214,	0.997,	1.056],
#         [1.257,	0.727,	0,	    2.809,	2.22,	2.342,	1.088,	0.965,	0.807],
#         [1.671,	2.119,	2.809,	0,      0.601,	0.54,	3.135,	2.908,	3.087],
#         [1.09,	1.526,	2.22,	0.601,	0,	    0.331,	2.563,	2.338,	2.5],
#         [1.315,	1.689,	2.342,	0.54,	0.331,	0,	    2.797,	2.567,	2.708],
#         [1.484,	1.214,	1.088,	3.135,	2.563,	2.797,	0,	    0.275,	0.298],
#         [1.253,	0.997,	0.965,	2.908,	2.338,	2.567,	0.275,	0,	    0.343],
#         [1.418,	1.056,	0.807,	3.087,	2.5,	2.708,	0.298,	0.343,	0,]])
# colnames = ['O1','O2','O3','O4','O5','O6','O7','O8','O9']


distArray = ssd.squareform(data)

z = linkage(distArray, method='complete', metric='euclidean')

plt.figure(figsize=(10, 7))
dendrogram(z,
            labels=colnames,
            distance_sort=True,
            orientation='top',)
plt.title(label="complete/maximum linkage")
plt.show()



z = linkage(distArray, method='single', metric='euclidean')

plt.figure(figsize=(10, 7))
dendrogram(z,
            labels=colnames,
            distance_sort=False,
            orientation='top',)
plt.title(label="single/minimum linkage")
plt.show()



z = linkage(distArray, method='average', metric='euclidean')

plt.figure(figsize=(10, 7))
dendrogram(z,
            labels=colnames,
            distance_sort=False,
            orientation='top',)
plt.title(label="average linkage")
plt.show()

print("BE SURE YOU CHECK THE CORRECT PLOT WITH THE DESIRED LINKAGE")
# nearestIndex = numpy.argsort(nearestList)[0]

# return nearestList

# mergeShortest(data)