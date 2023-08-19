import requests

def fetch_gifs():
    # Build the Gif URL using f-strings and variables
    search_query = "hilarious"
    rating = "g"
    api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
    url = f"https://api.giphy.com/v1/gifs/search?q={search_query}&rating={rating}&api_key={api_key}"

    # Fetch data from the URL
    response = requests.get(url)

    # Check if the status code is 200 (OK)
    if response.status_code == 200:
        # Get the JSON data
        data = response.json()

        # Filter gifs with height bigger than 100
        gifs_filtered = [gif for gif in data["data"] if gif["images"]["fixed_height"]["height"] > "100"]

        # Return the length of the filtered gifs list
        length_filtered_gifs = len(gifs_filtered)

        # Return only the first 10 gifs
        first_10_gifs = gifs_filtered[:10]

        return first_10_gifs, length_filtered_gifs
    else:
        print("Failed to fetch gifs.")
        return None

def main():
    gifs, length = fetch_gifs()
    if gifs:
        print("Fetched Gifs:")
        for gif in gifs:
            print(gif["url"])
        print(f"Total gifs with height > 100: {length}")

if __name__ == "__main__":
    main()
