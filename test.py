import json
from pprint import pprint

cuisines = []
ingredients = []
partition = []

with open('train.json') as data_file:    
    data = json.load(data_file)

for recipe in data:
  cuisines.append(recipe["cuisine"])
  for ingredient in recipe["ingredients"]:
    ingredients.append(ingredient)

#creates a list of unique cuisines and ingredients
cuisines = list(set(cuisines))
ingredients = list(set(ingredients))
#copies data to partition, will use this partition during gini calculation
partition.extend(data);

#partition function
def Partition(e_ingredient, source):
  "takes an ingredient, produces a partition that includes all those ingredients from the source partition"
  newPartition = []
  for recipe in source:
    if any(e_ingredient in ingredients for ingredients in recipe["ingredients"]):
      newPartition.append(recipe)
  return newPartition;

#tree node
class TreeNode:
  "these are individual nodes in a tree, should contain an ingredient or decision and yes or no functions to return the next node"
  def __init__(self, item):
    self.content = item
    self.yes = 0
    self.no = 0
  def SetYes(self, node):
    self.yes = node
  def SetNo(self, node):
    self.no = node
  def GetYes(self):
    return self.yes
  def GetNo(self):
    return self.no

#tree maintenance
class DecisionTree:
  "root only this is needed because we only care about whether or not an ingredient in included in a recipe, use node yes or no for traversal"
  root = 0 #initialize root to empty
  def __init__(self, node):
    root = node
  def SetRoot(self, node):
    root = node
  def GetRoot(self):
    return root

#GiniFunction
def Gini(partition, ingredient):
  "takes a partition and an ingredient, and provides the gini index of that ingredient"
  partitionTotal = len(partition)
  yeses = [recipe for recipe in partition if ingredient in recipe["ingredients"]] #find recipes with ingredient
  yesCount = len(yeses) #count how many recipes in the partition contain matching | yescount
  nos = [recipe for recipe in partition if ingredient not in recipe["ingredients"]] #find recipes without ingredient
  noCount = len(nos) #nocount
  #count how many recipes that is cuisine1 that has ingredient, repeat for all cuisines | cuisine1...
  for cuisine in cuisines:
    
  #subtract from total partition to find how many recipes do not | no count
  return;

Gini(partition, "other")

#Tests
#pprint(Partition("cooking cream", partition)) #test for partition function
#pprint(ingredients); #test for creating all nonduplicating ingredients list
#End Tests


#Misc Notes
#print data[0]["ingredients"][1] #prints first ingredient of first food
#print data[0]["cuisine"] #prints cuisine of the first food

#Algorithm Notes
#Gini(total) = 1 - (cuisine1/totalcount)^2 - ...

#Gini(ingredient:yes or no)(partition): yescount/partitiontotal ( 1 - (cuisine1/yescount)^2 - (cuisine2/yescount)^2)...) + nocount/partitiontotal ( 1 - (cuisine1/nocount)^2...)
