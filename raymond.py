import json

with open('trainSnip.json') as data_file:    
    data = json.load(data_file)
	
#print data[0]['id'], data[0]['cuisine']	#cuisine
#print data[1]['id'], data[1]['ingredients']	#all ingredients
#print data[1]['id'], data[1]['ingredients'][0] #only first ingredient
#print data[8]['id'], data[8]['cuisine']	#cuisine this should by 16903 and mexican

cuisines_count = {}
for i in range(len(data)):
	print data[i]['id'], data[i]['cuisine']
	if cuisines_count.has_key(data[i]['cuisine']):
		cuisines_count[data[i]['cuisine']] = cuisines_count[data[i]['cuisine']] + 1
	else:
		cuisines_count[data[i]['cuisine']] = 1

for key, value in cuisines_count.iteritems():
	print key, value
