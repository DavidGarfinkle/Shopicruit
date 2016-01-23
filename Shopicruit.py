#!usr/bin/python
import json
import urllib
import pprint
pp = pprint.PrettyPrinter(indent=2)

#Fetch and parse the store's JSON data
url = 'http://shopicruit.myshopify.com/products.json'
file_obj = urllib.urlopen(url)
json_obj = file_obj.read()
parsed_json = json.loads(json_obj)

pp.pprint(parsed_json)

merch = []
for product in parsed_json['products']:
	t = product['product_type']
	if t == 'Computer' or t == 'Keyboard': 
		for index in range(len(product['variants'])): #loop through all keyboard/computer variants
			if product['variants'][index]['available']: #check to see this variant is available
				merch.append((float(product['variants'][index]['grams']), float(product['variants'][index]['price'])))
				print (t, "id " + str(product['variants'][index]['id'])) #prints current product type

#NOTE weight is in GRAMS, cost is in Kettleman's bagels. mmm bagels...
print "If you buy everything: "
print merch
(weight, cost) = (0,0)
for pair in merch:
	weight += pair[0] / 1000 #convert to kilograms	
	cost += pair[1]	
print "then you'll need to carry " + str(weight) + " kg at a cost of " + str(cost) + " bagels."

if (weight / 100) < 100:
	print "Yay! We are done."
else:
	print "total weight exceeds backpack capacity! go back and implement the knapsack algorithm"
