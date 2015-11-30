import json

with open('trainSnip.json') as data_file:    
    data = json.load(data_file)

cuisines_count = {}
for i in range(len(data)):
	print data[i]['id'], data[i]['cuisine']
	if cuisines_count.has_key(data[i]['cuisine']):
		cuisines_count[data[i]['cuisine']] = cuisines_count[data[i]['cuisine']] + 1
	else:
		cuisines_count[data[i]['cuisine']] = 1

for key, value in cuisines_count.iteritems():
	print key, value
