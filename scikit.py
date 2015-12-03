# -*- coding: utf-8 -*-
import json
import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
vec = DictVectorizer()

with open('train.json') as data_file:    
    data = json.load(data_file)

clf = tree.DecisionTreeClassifier()

#get list of unique ingredients and cuisines of current local partition
cuisines = []
ingredients = []
for recipe in data:
    cuisines.append(recipe["cuisine"])
    for ingredient in recipe["ingredients"]:
        ingredients.append(ingredient)
ingredients = list(set(ingredients))
cuisines = list(set(cuisines))

#have to move cuisine to the end and remove id
dataSet = []
targetSet = []
for recipe in data:
    item = {}
    targetItem = {}
    for ing in ingredients:
        item[ing] = 0
    for c in cuisines:
        targetItem[c] = 0
    for ingredient in recipe["ingredients"]:
        item[ingredient] = 1
    targetItem[recipe["cuisine"]] = 1
    dataSet.append(item)
    targetSet.append(targetItem)

#transform to vector arrays
dataTrain = vec.fit_transform(dataSet).toarray()
targetTrain = vec.fit_transform(targetSet).toarray()
cuisineArray = vec.get_feature_names()

clf.fit(dataTrain, targetTrain)

with open('test.json') as testfile:    
    test = json.load(testfile)
testIngredients = []
testIds = []
for t in test:
    itemIng = {}
    for i in ingredients:
        itemIng[i] = 0
    for ingredient in t["ingredients"]:
        if ingredient in ingredients:
            itemIng[ingredient] = 1
    testIngredients.append(itemIng)
    testIds.append(t["id"])
dataTest = []
for test in testIngredients:
    dataTest.extend(vec.fit_transform(test).toarray())
resultVec = clf.predict(dataTest)

#parse the results
results = []
for r in resultVec:
    index = 0
    for c in r:
        if c == 1:
            results.append(cuisineArray[index])
        index = index + 1
        
final = {}
index = 0
for ids in testIds:
    final[ids] = results[index]
    index = index + 1
    
writer = csv.writer(open('results1.csv', 'wb'))
for key, value in final.items():
   writer.writerow([key, value])

