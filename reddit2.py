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

import requests
import time

#We set limits here so the user doesn't exceed the rate limit set by Reddit
MAX_REQUESTS = 60 #User will have to wait 60 seconds when rate limit is reached
used_requests = 0
start_time = time.time()

while True:
    #Prompt for user to enter desired subreddit they want to check out
    subreddit = input("\nEnter name of subreddit (or exit): ")
    if subreddit == "exit":
        break

    elapsed_time = time.time() - start_time

    if used_requests >= MAX_REQUESTS:
        print("Rate limit reached. Please wait 60 seconds")
        time.sleep(60) #60 second cooldown when rate limit of 60 is exceeded
        used_requests = 0
        start_time = time.time() #Time track

    URL = f"https://www.reddit.com/r/{subreddit}/about.json"

    HEADERS = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36^"
    }

    print(f"\n Request for r/{subreddit} being processed....")

    r = requests.get(URL, headers=HEADERS)
    used_requests += 1 #Max requests before reaching limit is 60

    if r.status_code == 200:
        data = r.json().get("data", {})
        print("-" * 50)
        print(f"Name: {data.get('display_name', 'N/A')}")
        print(f"Description: {data.get('public_description', 'N/A')}")
        print(f"Subscribers: {data.get('description', 'N/A')}")
        print(f"Subscribers: {data.get('subscribers', 'N/A')}")
        print("-" *50)
        print(f"Request {used_requests}/{MAX_REQUESTS}")
    else:
        print(f"Subreddit: '{subreddit}' not found")