#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('items.faix', 'r')

soup = BeautifulSoup(file, 'xml')

items = soup.find_all("item", { 'id': True })

for item in items:
	id = item['id']

	item_value = item.find('item').text
	type_value = item.find('type').text
	rarity_value = item.find('rarity')['value']


	print(f"{id}\t {item_value}\t\t{type_value}\t{rarity_value}")
