import json
from pprint import pprint

with open('train.json') as data_file:    
    data = json.load(data_file)

cuisines = {}
for i in range(len(data)):
	cuisineType = data[i]['cuisine']
	ingredients = data[i]['ingredients']
	if cuisines.has_key(cuisineType):
		for j in range(len(ingredients)):
			if cuisines[cuisineType].has_key(ingredients[j]):
				cuisines[cuisineType][ingredients[j]] = cuisines[cuisineType][ingredients[j]] + 1
			else:
				cuisines[cuisineType][ingredients[j]] = 1
				
	else:
		cuisines[cuisineType] = {}
		for j in range(len(ingredients)):
			cuisines[cuisineType][ingredients[j]] = 1

for key, value in cuisines.iteritems():
	print key
	pprint(value)