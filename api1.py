# Fetches data for Pokémon ID 1 (Bulbasaur) from the PokéAPI
import requests

url = "https://pokeapi.co/api/v2/pokemon/1/" 
response = requests.get(url)
pokemon_data = response.json()
name = pokemon_data['name'].capitalize()
height = pokemon_data['height']  # dm
weight = pokemon_data['weight']  # hg

print(f"Name: {name}")
print(f"ID: {pokemon_data['id']}")
print(f"Height: {height / 10:.1f} meters")
print(f"Weight: {weight / 10:.1f} kg")
print(f"Base Experience: {pokemon_data['base_experience']}")