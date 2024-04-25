#!/usr/bin/python3

from xml.dom import minidom

faix = minidom.parse('items.faix')

root = faix.getElementsByTagName('items')
root = root[0].childNodes

for element in root:
	if element.nodeType == element.TEXT_NODE:
		continue

	id = element.getAttribute('id')

	name = element.getElementsByTagName('item')
	name_value = name[0].firstChild.nodeValue

	type = element.getElementsByTagName('type')
	type_value = type[0].firstChild.nodeValue

	rarity = element.getElementsByTagName('rarity')
	rarity_value = rarity[0].getAttribute('value')


	print(f"{id}\t {name_value}\t {type_value}\t {rarity_value}")

	print("-"*64)
