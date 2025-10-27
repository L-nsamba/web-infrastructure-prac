import requests

SHOW = "breaking"

URL = f"https://api.tvmaze.com/search/shows?q={SHOW}"

response = requests.get(URL)
data = response.json()

show_name = (data[0]["show"]["name"])
show_rating = (data[0]["show"]["rating"])
show_description = (data[0]["show"]["summary"])
show_image = (data[0]["show"]["image"])
show_image_url = show_image["medium"] if show_image else ""

print(f"\nShow Name: {show_name}")
print(f"\nShow Rating: {show_rating['average']}")
print(f"\nShow Description: {show_description}")

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TV MAZE EXTRACTING BREAKING BAD API</title>
</head>
<body>
    <img src="{show_image_url}" alt="{show_image}">
    <h1>{show_name}</h1>
    <p>{show_rating}</p>
    <p>{show_description}</p>
</body>
</html>
"""

with open("show.html", "w") as file:
    file.write(html_content)