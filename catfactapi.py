import requests

url = "https://catfact.ninja/fact"

#Creation of a list to store each fact
facts = []

for i in range(5):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #Retrival of fact from json
        fact = data["fact"]
        #Adding the latest fact to the list
        facts.append(fact)
        print(f"Fact {i + 1} fetched successfully.")
    else:
        print(f"Server error: {response.status_code}")

print("\nAll Cat Facts")
for i, fact in enumerate(facts, start=1):
    print(f"{i}. {fact}")