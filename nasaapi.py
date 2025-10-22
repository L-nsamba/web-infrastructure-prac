import requests
import os
from dotenv import load_dotenv

#Loading environmental variables
load_dotenv()

url = "https://api.nasa.gov/neo/rest/v1/feed"

#Accessing the api key from the env file
api_key = os.getenv("NASA_API_KEY")

queries = {
    "start_date": "2015-09-08",
    "end_date": "2015-09-09",
    "api_key": api_key
}

response = requests.get(url, params=queries)

#Determining whether the server is good to go
if response.status_code == 200:
    data = response.json()
    print("Request successful!\n")

    #Obtaining the parameters to reference from the json file
    for date, asteriods in data["near_earth_objects"].items():
        print(f"Date: {date}")
        print(f"Number of asteriods detected: {len(asteriods)}\n")

        for asteriod in asteriods:
            name = asteriod["name"]
            distance = float(asteriod["close_approach_data"][0]["miss_distance"]["kilometers"])
            distance = round(distance, 2)
            print(f"Name: {name}")
            print(f"Closet distance: {distance} km\n")

else:
    print(f"Status code issue {response.status_code} \n")