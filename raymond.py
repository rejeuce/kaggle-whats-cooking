import json

with open('train.json') as data_file:    
    data = json.load(data_file)
	
print data[0]['id'], data[0]['cuisine']	#cuisine
print data[1]['id'], data[1]['ingredients']	#all ingredients
print data[1]['id'], data[1]['ingredients'][0] #only first ingredient
print data[8]['id'], data[8]['cuisine']	#cuisine this should by 16903 and mexican