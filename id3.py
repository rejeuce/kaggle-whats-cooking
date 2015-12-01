import json
import math
from pprint import pprint

with open('trainSnip.json') as data_file:
    data = json.load(data_file)

def split_data(data, x):
	leftData = []
	rightData = []
	for i in range(len(data)):
		if x in data[i]['ingredients']:
			rightData.append(data[i])
		else:
			leftData.append(data[i])
	return (leftData, rightData)
	
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

def build_tree(data):
	#if data is empty set cuisine then break
	#if len(data) == 0:
	#	return None
	
	cCount, iCount, iList = parse_data(data)
	
	attribute, entropy, cuisine = attr_select(cCount, iCount, iList) # returns the largest info gain/entropy
	
	tree = {}	# tree is represented with a dictionary of dictionaries
	if entropy == 0.0:
		tree[0] = cuisine
		return tree
	
	left, right = split_data(data, attribute)
	tree[0] = attribute
	tree[1] = build_tree(left)
	tree[2] = build_tree(right)

	return tree
	
def attr_select(cCount, iCount, iList):
	entropies = {}
	for a in iList:
		entropies[a] = entropy(a, iCount, cCount)
	attr = min(entropies, key=entropies.get)
	cuisine = cCount.items()[0]
	return (attr,entropies[attr],cuisine)

def parse_data(data):
	cCounts = {}
	iCounts = {}
	ingrList = []
	for i in range(len(data)):
		cuisineType = data[i]['cuisine']
		ingredients = data[i]['ingredients']
		ingrList = ingrList + ingredients
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
				
	return (cCounts, iCounts, ingrList)
	
def decision_tree(dt, ingreds):
	if not isinstance(dt, dict):
		return dt
	else:
		if dt[0] in ingreds:
			return decision_tree(dt[2], ingreds)
		else:
			return decision_tree(dt[1], ingreds)
	
def classify():
	with open('trainSnip.json') as data_file:
		trainData = json.load(data_file)

	with open('test.json') as data_file:
		testData = json.load(data_file)
	
	#dTree = build_tree(trainData)
	
	f = open("submission.csv", "w")
	for i in range(len(testData)):
		id = testData[i]['id']
		ingrs = testData[i]['ingredients']
		#cuisine = decision_tree(dTree, ingrs)
		cuisine = 'italian'
		f.write("%d,%s\n" % (id,cuisine))
	f.close()