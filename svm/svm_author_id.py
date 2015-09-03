#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#print 'Training set size', len(features_train)
#print 'Test set size', len(features_test)

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel='rbf', C=10000.)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
labels_prediction = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

print '10:', labels_prediction[10]
print '26:', labels_prediction[26]
print '50:', labels_prediction[50]

print 'Count 0:', labels_prediction.tolist().count(0)
print 'Count 1:', labels_prediction.tolist().count(1)

precision = clf.score(features_test, labels_test)

print 'Precision', precision
