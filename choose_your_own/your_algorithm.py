#!/usr/bin/python

#import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
#from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
#grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
#bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
#grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
#bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
#plt.xlim(0.0, 1.0)
#plt.ylim(0.0, 1.0)
#plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
#plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
#plt.legend()
#plt.xlabel("bumpiness")
#plt.ylabel("grade")
#plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import AdaBoostClassifier as ABC
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.svm import SVC

# KNNC: best acc = 0.936: n_neighbors = 20
# clf = KNC(n_neighbors=20)
# clf.fit(features_train, labels_train)
# acc = clf.score(features_test, labels_test)
# print acc

# RFC: best acc = 0.94
# for i in range(1,20):
#     for j in range(1, 20):
#         clf = RFC(n_estimators=i, min_samples_split=j, n_jobs=4)
#         clf.fit(features_train, labels_train)
        
#         acc = clf.score(features_test, labels_test)

#         if acc > 0.93:
# 	    	print str(i), str(j), acc

# RFC: best acc = 0.94
for i in [x * 0.1 for x in range(1, 11)]:
	clf = SVC(C=i, kernel='linear')
	clf.fit(features_train, labels_train)

	acc = clf.score(features_test, labels_test)

	if acc > 0.93:
		print str(i), str(j), acc

#try:
#    prettyPicture(clf, features_test, labels_test)
#except NameError, e:
#    print e.message
#    pass
