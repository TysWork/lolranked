import time 
import requests

API_KEY = "RGAPI-b45475e3-71ea-46ff-807c-6cc1f7ee23b6"
HEADERS = {"X-Riot-Token": API_KEY}

def request_delay(url):
    while True: 
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 429:  #Too many requests 
            retry_after = int(response.headers.get("Retry-After", 5))
            print(f"Rate limit exceeded. Retrying after {retry_after} seconds.")
            time.sleep(retry_after)
            continue
        if response.status_code == 401:
            print("401 Unauthorized. Check your API key.", response.text)
        response.raise_for_status()
        time.sleep(1.3) 
        return response 