#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

salary = [[x[0]] for x in data]
bonus = [x[1] for x in data]

# new_len = int(0.9 * len(bonus))
new_len = len(bonus) - 5
while len(bonus) > new_len:
	# plt.scatter(salary, bonus)
	# plt.show()

	avg = sum([x[0] for x in salary]) / len(salary)
	diff = [abs(x-avg) for x in bonus]
	max_diff_index = diff.index(max(diff))

	s_salary = salary[max_diff_index][0]
	s_bonus = bonus[max_diff_index]

	salary.pop(max_diff_index)
	bonus.pop(max_diff_index)

	for key in data_dict:
		value = data_dict[key]

		if value['salary'] != 'NaN' and float(value['salary']) == s_salary:
			print 'Key is', key
