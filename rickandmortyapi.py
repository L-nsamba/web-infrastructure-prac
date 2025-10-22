import requests

url = "https://rickandmortyapi.com/api"
character_url = "https://rickandmortyapi.com/api/character"
location_url = "https://rickandmortyapi.com/api/location"
episode_url = "https://rickandmortyapi.com/api/episode"

response = requests.get(episode_url) #Insert the url of your choice from the above three


if response.status_code == 200:
    data = response.json()
    # characters = data["results"]
    #locations = data["results"]
    episodes = data["results"]

    # for character in characters:
    #     print(character["name"], "-", character["species"])

    # for location in locations:
    #     print(location["name"], "-", location["type"])

    for episode in episodes:
        print(episode["name"], "-", episode["air_date"])

else:
    print(f"Server error, {response.status_code}")