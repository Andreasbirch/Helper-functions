import numpy
from sklearn.cluster import KMeans
import sys
colnamesText = input("Type the names of each Observation in the order they appear, separated by spaces \nFor example: O1 O3 O4 O2\n")
rawTextInput = input("Paste the values of each observation, separated by spaces \nFor example: 3.14 2.2 1.1 0.5\n")
k = input("Type final amount of clusters, k: ")
centroids = input("Type the initial centroid values, separated by spaces only: \nFor example: 0.8 1.1\n")
k = int(k)


data = rawTextInput.split(' ')
data = numpy.asarray(numpy.reshape(data, (-1,1)))
data = data.astype(float)

# Breakdown colnames
# colnamesText = "O8 O6 O4 O2 O3 O1 O5 O7"
colnamesText = colnamesText.replace('O','')
colnamesText = colnamesText.replace('o','')
colnames = colnamesText.split(' ')

centroids = centroids.split(' ')
centroids = numpy.asarray(numpy.reshape(centroids, (-1,1)))
centroids = centroids.astype(float)
# Done loading data



# FOR MANUAL INPUT UNCOMMENT AND INSERT HERE
# Testinput Spring2017
# data = [[19.4], 
#         [30.3], 
#         [34.2], 
#         [38.3], 
#         [40.1], 
#         [42.0],
#         [50.9],
#         [68.6]]
# centroids = [[19.4],
#              [30.3]]
# colnames = ['O8', 'O6', 'O4', 'O2', 'O3', 'O1', 'O5', 'O7']
# k = 2


kmeans = KMeans(n_clusters = k, init=centroids, n_init=1)
kmeans.fit(data)
kmeans.predict(data.reshape(-1,1))
clusters = kmeans.predict(data.reshape(-1,1))
cluster_centers = kmeans.cluster_centers_


stri = ""
for i in range(k):
    stri = stri + "{"
    for j in range(len(clusters)):
        if(clusters[j] == i):
            try:
                if(clusters[j+1] != i):
                    stri = stri + colnames[j]
                else :
                    stri = stri + colnames[j] + ", "
            except(IndexError):
                stri = stri + colnames[j]
    stri = stri + "} "


colnames = stri.split("} {")
for i in range(len(colnames)):
    colnames[i] = colnames[i].replace('{', '')
    colnames[i] = colnames[i].replace(" }", '')
    colnames[i] = colnames[i].replace('}', '')
    colnames[i] = colnames[i].split(', ')
    colnames[i] = sorted(colnames[i])


stri = ""
for i in range(k):
    stri = stri + "{"
    for j in range(len(colnames[i])):
        if(j != len(colnames[i])-1):
            stri = stri + 'O' + colnames[i][j] + ", "
        else: 
            stri = stri + 'O' + colnames[i][j]
    stri = stri + "} "
    
centroidstri = ""
for i in range(k):
    if(i != k -1 ):
        centroidstri = centroidstri + str(round(cluster_centers[i][0], 2)) + ", "
    else:
        centroidstri = centroidstri + str(round(cluster_centers[i][0], 2))
        
print("Clusters are:")
print(stri)

print("Centroids become: ")
print(centroidstri)