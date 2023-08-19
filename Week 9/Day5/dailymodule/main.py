import requests
import time

def get_webpage_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        response_time = time.time() - start_time
        return response_time
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Test the function with multiple sites
sites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]
for site in sites:
    load_time = get_webpage_load_time(site)
    if load_time is not None:
        print(f"Webpage: {site} | Load Time: {load_time:.2f} seconds")
