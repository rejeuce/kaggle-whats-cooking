import pandas

train = pandas.read_json('trainSnip.json')
id = train['id']
cuisine = train['cuisine']
ingredients = train['ingredients']
ingArr = []
for x in ingredients:
	ingArr.append(ingredients[x])
