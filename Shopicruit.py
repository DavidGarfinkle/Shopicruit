#!usr/bin/python
import json
import urllib

#import pprint
#pp = pprint.PrettyPrinter(indent=2)

#Fetch and parse the store's JSON data
url = 'http://shopicruit.myshopify.com/products.json'
file_obj = urllib.urlopen(url)
json_obj = file_obj.read()
parsed_json = json.loads(json_obj)

#pp.pprint(parsed_json)

(weight, cost) = (0,0)
for product in parsed_json['products']:
	t = product['product_type']
	if t == 'Computer' or t == 'Keyboard':
		weight += float(product['variants'][0]['grams'])
		cost += float(product['variants'][0]['price'])
		print t #prints current product type

#NOTE weight is in GRAMS, cost is in Kettleman's bagels. mmm bagels...
print (weight / 1000, cost)
