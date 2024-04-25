#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx', 'r')

soup = BeautifulSoup(file, 'xml')

characters = soup.find_all("character")


file.close()

title = "Bienvenido/a a Fary's Adventure"

print(title)
print("="*len(title))

print("\n¿Quién quieres ser?\n")

for character in characters:
	print(f"{character['id']}\t {character.find('name').text}")

encontrado = False
while not encontrado:
	id = input("\nIntroduce un número: ")
	file = open('characters.facx', 'r')
	
	soup = BeautifulSoup(file, 'xml')

	file.close()

	character = soup.find('character', {'id': id})

	if not character:
		print("Error: id no encontrado")
	else:
		encontrado = True

print("\nEl personaje escogido es:\n")
print(f"\tNombre: {character.find('name').text}")
print(f"\tEdad: {character.find('age').text}")
print(f"\tGénero: {character.find('gender')['value']}")
print(f"\tNivel: {character.find('level')['value']}")
file = open('characters_items.facix', 'r')
soup2 = BeautifulSoup(file, 'xml')
character_item = soup2.find('character_item', {'id': id})
print(f"\tId del item: {character_item.find('item')['id']}")
id_items = character_item.find('item')['id']


file = open('items.faix', 'r')
soup3 = BeautifulSoup(file, 'xml')
item = soup3.find('character_item', {'id': id})

items = soup3.find_all("item", {'id' : id_items})

for item in items:
	id = item['id']

	item_value = item.find('item').text
	type_value = item.find('type').text
	rarity_value = item.find('rarity')['value']
	print(f"{id}\t {item_value}\t\t{type_value}\t{rarity_value}")


