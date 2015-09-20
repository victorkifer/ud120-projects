#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

predicted = clf.predict(X_test)

print clf.score(X_test, y_test)

pois_predicted = sum([1 for x in predicted if x == 1])
total_people = len(predicted)
print pois_predicted
print total_people

true_pos = sum([1 for x,y in zip(predicted, y_test) if x == 1 and y == 1])
print true_pos

from sklearn.metrics import precision_score, recall_score
precision = precision_score(y_test, predicted)
recall = recall_score(y_test, predicted)

print 'Precision', precision
print 'Recall', recall