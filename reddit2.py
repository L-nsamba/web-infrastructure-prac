import requests

# """
# curl ^"https://www.reddit.com/r/programming/about/^" ^
#   -H ^"accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7^" ^
#   -H ^"accept-language: en-US,en;q=0.9^" ^
#   -H ^"cache-control: max-age=0^" ^
#   -b ^"edgebucket=4PzWTbsXwRtamcL4tj; loid=000000001jjm98nj7f.2.1739902494770.Z0FBQUFBQm50TTRla2RHc183anpFNzJNTjNHMEhBYy02ZUV0dmFxbC1FS195U2M0WnhiOU1YN2tNc1B6eXVvM3JUWHE5Q21oNnRPYlROUmFtSTdaNlduREx5Slc3OEROM1haeHpmTXc4Mms0d0R0b2tucnFHSDdfcFNGMkdBejFyZlpoX01OUDZJc04; csv=2; pc=38; csrf_token=107f95488375f65ce916108b75cadce6; token_v2=eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJsb2lkIiwiZXhwIjoxNzYxMzA4NTA0LjA5Mzc3NCwiaWF0IjoxNzYxMjIyMTA0LjA5Mzc3MywianRpIjoiQmtxdUNPVU9hSGR4UVE4NV9GZHpmUFl0Wm5IVG5nIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml8xamptOThuajdmIiwibGNhIjoxNzM5OTAyNDk0NzcwLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5feldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJmbG8iOjF9.RJB1ain6PwXAFTnKu94QP4yvOw5KxmKCFfggVhGtjmOi-cHCu0tSM6M7hAtBY_ur9HGuEeXjviuS-dwJVEd9Im-UX0Ii5d8umMlnZaIK2lkHZMt145ZMlgeyfErP3NxO2LvfHFP_lZKshGdIgkvs5MNtFy_HrjMG6O6dOeefBmRCrV7E0Mq9G3QnE7hBxWagbG_ltr-2TloDgArAcAXS-wxG01tVY7ZDN9sqqMO5WzV19U_gnkSgi_rFNchOPnIeJMSaeJ8ABpzwUKvenleWdIfrY2xyl10tUhV1wdOM2io5dz6mXVZFQTPuc-OEi0mDTGTRlQsULG5IEtnWcM9OvQ; g_state=^{^\^"i_l^\^":0,^\^"i_ll^\^":1761222109590,^\^"i_b^\^":^\^"gslRdBMdh9A3nzsex6rOtt0U9PJ8QSniCQZkqq3RNAI^\^"^}; session_tracker=qconmjciliqgmhrfid.0.1761222116454.Z0FBQUFBQm8taDNrdEJCY0FDckVFdWJVZ2ZDcGtlclJaT3puWmhtajltdmZ0cGR0UndmQ0JyWHhJemZtRjdmUDFaMktZc3ZleTZZRHBhVU0tdU1tUWs4dkxzbjlxWUtOTXR2Tm91OEVLWUdLenVJVnU2ajAzd19RYlVxMnhYYUJvSHBGVkNQNDY3di0^" ^
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