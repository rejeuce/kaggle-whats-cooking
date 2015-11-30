

import pandas
import numpy

trainSnip = pandas.read_json("trainSnip.json")	#import a snippet of large training data
trainSnip.head() 			#shows how pandas puts the json in nicer format

ingredientSnip = trainSnip['ingredients']
 
ingredientSnip.head()

''' the latter has a "double" array of the ingrdients for each recipe

0    [romaine lettuce, black olives, grape tomatoes...
1    [plain flour, ground pepper, salt, tomatoes, g...
2    [eggs, pepper, salt, mayonaise, cooking oil, g...
3                  [water, vegetable oil, wheat, salt]
4    [black pepper, shallots, cornflour, cayenne pe...
5    [plain flour, sugar, butter, eggs, fresh ginge...
6    [olive oil, salt, medium shrimp, pepper, garli...
7    [sugar, pistachio nuts, white almond bark, flo...

'''
