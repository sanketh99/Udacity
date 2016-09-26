#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

poi_names = [
	"Lay, Kenneth",
	"Skilling, Jeffrey",
	"Howard, Kevin",
	"Krautz, Michael",
	"Yeager, Scott",
	"Hirko, Joseph",
	"Shelby, Rex",
	"Bermingham, David",
	"Darby, Giles",
	"Mulgrew, Gary",
	"Bayley, Daniel",
	"Brown, James",
	"Furst, Robert",
	"Fuhs, William",
	"Causey, Richard",
	"Calger, Christopher",
	"DeSpain, Timothy",
	"Hannon, Kevin",
	"Koenig, Mark",
	"Forney, John",
	"Rice, Kenneth",
	"Rieker, Paula",
	"Fastow, Lea",
	"Fastow, Andrew",
	"Delainey, David",
	"Glisan, Ben",
	"Richter, Jeffrey",
	"Lawyer, Larry",
	"Belden, Timothy",
	"Kopper, Michael",
	"Duncan, David",
	"Bowen, Raymond",
	"Colwell, Wesley",
	"Boyle, Dan",
	"Loehr, Christopher"
]

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

name_list = {}
for i in enron_data:
	if i != 'TOTAL':
		name_split = i.split()
		name = name_split[0].lower().capitalize() + ", " + name_split[1].lower().capitalize()
		name_list[name] = i


def convertPOI_Names():
	converted_poi_names = []
	for i in poi_names:
		name = i .split(', ')
		name = name[0].upper() + " " + name[1].upper()
		converted_poi_names.append(name)
	return converted_poi_names

def obtainDataForPOIs():
	data = {}
	enron_names = []
	for i in name_list:
		enron_names.append(i)

	POIs_in_enron_data = set(enron_names).intersection(poi_names)
	for i in POIs_in_enron_data:
		data[name_list[i]] = enron_data[name_list[i]]
	return data

print len(enron_data)
eh = 0
for i in enron_data:
	if enron_data[i]['total_payments'] == 'NaN':
		eh += 1
print eh