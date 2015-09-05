#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

no_of_people = len(enron_data)
print 'No of People', no_of_people

POI = sum([1 for x in enron_data.values() if x['poi'] == True])
print 'POI', POI

print 'James Prentice', enron_data['PRENTICE JAMES']['total_stock_value']
print 'Wesley Colwell', enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print 'Jeffrey Skilling', enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print 'Lay', enron_data['LAY KENNETH L']['total_payments']
print 'Skilling', enron_data['SKILLING JEFFREY K']['total_payments']
print 'Fastow', enron_data['FASTOW ANDREW S']['total_payments']

with_known_salary = sum([1 for x in enron_data.values() if x['salary'] != 'NaN'])
print 'With known salary', with_known_salary

with_known_email = sum([1 for x in enron_data.values() if x['email_address'] != 'NaN'])
print 'With known email', with_known_email

with_unknown_total_payments = sum([1 for x in enron_data.values() if x['total_payments'] == 'NaN'])
print 'With unknown total payments', with_unknown_total_payments
print 'With unknown total payments, in per cents', with_unknown_total_payments * 1. / len(enron_data)

poi_with_unknown_total_payments = sum([1 for x in enron_data.values() if x['total_payments'] == 'NaN' and x['poi'] == True])
print 'POI with unknown total payments', poi_with_unknown_total_payments
print 'POI with unknown total payments, in per cent', poi_with_unknown_total_payments * 1. / POI

people_added = 10
new_no_of_people = no_of_people + people_added
new_with_unknown_total_payments = with_unknown_total_payments + people_added
print 'New No of People', new_no_of_people
print 'New with unknown total payments', new_with_unknown_total_payments

new_no_of_poi = POI + people_added
new_poi_with_unknown_total_payments = poi_with_unknown_total_payments + people_added
print 'New POI', new_no_of_poi
print 'New POI with unknown total payments', new_poi_with_unknown_total_payments

