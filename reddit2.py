import requests

# """
# curl ^"https://www.reddit.com/r/programming/about/^" ^
#   -H ^"accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7^" ^
#   -H ^"accept-language: en-US,en;q=0.9^" ^
#   -H ^"cache-control: max-age=0^" ^
#   -H ^"priority: u=0, i^" ^
#   -H ^"sec-ch-ua: ^\^"Google Chrome^\^";v=^\^"141^\^", ^\^"Not?A_Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"141^\^"^" ^
#   -H ^"sec-ch-ua-mobile: ?1^" ^
#   -H ^"sec-ch-ua-platform: ^\^"Android^\^"^" ^
#   -H ^"sec-fetch-dest: document^" ^
#   -H ^"sec-fetch-mode: navigate^" ^
#   -H ^"sec-fetch-site: none^" ^
#   -H ^"sec-fetch-user: ?1^" ^
#   -H ^"upgrade-insecure-requests: 1^" ^
#   -H ^"user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36^"
# """

SUBREDDIT = "programming"
URL = f"https://www.reddit.com/r/{SUBREDDIT}/about.json"

HEADERS = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36^"
}

r = requests.get(URL, headers=HEADERS)

if r.status_code == 200:
    payload = r.json()

    info = payload["data"]

    print("-" *50)
    print(info["display_name"])
    print(info["description"])
    print(info["subscribers"])