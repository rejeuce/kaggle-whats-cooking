import json
import math
from pprint import pprint

with open('entropyTest.json') as data_file:
    data = json.load(data_file)

def parse_data(data):
	cCounts = {}
	iCounts = {}
	for i in range(len(data)):
		cuisineType = data[i]['cuisine']
		ingredients = data[i]['ingredients']
		
		if cCounts.has_key(data[i]['cuisine']):
			cCounts[data[i]['cuisine']] = cCounts[data[i]['cuisine']] + 1
		else:
			cCounts[data[i]['cuisine']] = 1
		
		if iCounts.has_key(cuisineType):
			for j in range(len(ingredients)):
				if iCounts[cuisineType].has_key(ingredients[j]):
					iCounts[cuisineType][ingredients[j]] = iCounts[cuisineType][ingredients[j]] + 1
				else:
					iCounts[cuisineType][ingredients[j]] = 1
					
		else:
			iCounts[cuisineType] = {}
			for j in range(len(ingredients)):
				iCounts[cuisineType][ingredients[j]] = 1
				
	return (cCounts, iCounts)
	
def info(arr):
	NumRecipes = 0.0			
	for i in range(len(arr)):
		NumRecipes = NumRecipes + arr[i]
	sum = 0.0
	for i in range(len(arr)):
		if arr[i] == 0.0:
			continue
		else:
			sum = sum + ( arr[i]/NumRecipes)* (1.0/math.log10(2.0)) * math.log10(arr[i]/NumRecipes)
	return -1.0 * sum

def entropy(ingredient, mapOfCuisIngred, mapOfCuis):
	NumRecipes = 0.0
	for x in mapOfCuis:
		NumRecipes = NumRecipes + mapOfCuis[x]
	NumWIngr = 0.0
	for x in mapOfCuisIngred:
		if ingredient in mapOfCuisIngred[x]:
			NumWIngr = NumWIngr + mapOfCuisIngred[x][ingredient]
	
	#create the arrays to pass to info that allows computation of information
	a = []
	b = []

	for x in mapOfCuisIngred:
		if ingredient in mapOfCuisIngred[x]:
			a.append(mapOfCuisIngred[x][ingredient])
	
	for x in mapOfCuisIngred:
		if ingredient in mapOfCuisIngred[x]:
			b.append(mapOfCuis[x] - mapOfCuisIngred[x][ingredient])

	Entr1 = 0
	Entr2 = 0

	Entr1 = (NumWIngr/NumRecipes)*info(a)
	Entr2 = ((NumRecipes - NumWIngr) / NumRecipes)* info(b)

	return Entr1 + Entr2

x,y = parse_data(data)