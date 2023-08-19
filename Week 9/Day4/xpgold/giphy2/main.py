import requests

API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
BASE_URL = "https://api.giphy.com/v1/gifs/search"
TRENDING_URL = "https://api.giphy.com/v1/gifs/trending"

def fetch_gifs(query):
    params = {
        "q": query,
        "api_key": API_KEY,
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        gifs = data.get("data", [])

        if not gifs:
            print("Couldn't find any relevant GIFs. Showing trending GIFs instead.")
            return fetch_trending_gifs()

        return [gif["url"] for gif in gifs]
    else:
        print("Failed to fetch gifs.")
        return None

def fetch_trending_gifs():
    params = {
        "api_key": API_KEY,
    }

    response = requests.get(TRENDING_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        gifs = data.get("data", [])

        return [gif["url"] for gif in gifs]
    else:
        print("Failed to fetch trending gifs.")
        return None

def main():
    search_query = input("Enter a term or phrase to find relevant GIFs: ")
    gifs = fetch_gifs(search_query)

    if gifs:
        print(f"\nRelevant GIFs for '{search_query}':")
        for gif in gifs:
            print(gif)
    else:
        print("No relevant GIFs found. Showing trending GIFs instead.")
        trending_gifs = fetch_trending_gifs()
        if trending_gifs:
            print("\nTrending GIFs of the day:")
            for gif in trending_gifs:
                print(gif)

if __name__ == "__main__":
    main()
