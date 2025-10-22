import requests

url = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(url)

if response.status_code == 200:
    pokemon_data = response.json()

    pokemon_info = pokemon_data["results"]

    for pokemon in pokemon_info:
        print(pokemon["name"], "-", pokemon["url"])
else:
    print(f"Status code error: {response.status_code}")

# ACCESSING INDIVIDUAL POKEMONS

# url = "https://pokeapi.co/api/v2/pokemon/2/"

# response = requests.get(url)

# if response.status_code == 200:
#     pokemon_data = response.json()

#     pokemon_info = pokemon_data["forms"]
#     #print(pokemon_info)

#     for pokemon in pokemon_info:
#         #print(pokemon["ability"]["name"], "-", pokemon["is_hidden"])
#         print(pokemon["name"])
# else:
#     print(f"Status code error: {response.status_code}")