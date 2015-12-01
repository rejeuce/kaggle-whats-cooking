import json
from pprint import pprint

with open('trainSnip.json') as data_file:
    data = json.load(data_file)
	
testTree = {}
testTree[0] = 'salt'
testTree[1] = 'salty dog'
testTree[2] = 'salty dog'


def split_data(data, x):
	leftData = []
	rightData = []
	for i in range(len(data)):
		if x in data[i]['ingredients']:
			rightData.append(data[i])
		else:
			leftData.append(data[i])
	return (leftData, rightData)

def build_tree(data):
	#if data is empty set cuisine then break
	if len(data) == 0:
		return None
	
	ccount, icount = parse_data(data)
	
	value = info_gain(ccount, icount) # returns the largest info gain/entropy
	left, right = split_data(data, value)
	
	tree = {}	# tree is represented with a dictionary of dictionaries
	tree[0] = value
	tree[1] = build_tree(left)
	tree[2] = build_tree(right)

	return tree
	
def info_gain(ccount, icount):
	return (None, None)

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
	
def decision_tree(dt, ingreds):
	while len(dt) > 1:
		if ingreds.has_key(dt[0]):
			dt = dt[2]
		else:
			dt = dt[1]
	return dt[0]
	
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