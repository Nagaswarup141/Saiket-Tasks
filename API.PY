import requests
print("Fetching data...")
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
print("Status Code:", response.status_code)  # debug
if response.status_code == 200:
    data = response.json()
    print("\n😂 Joke of the Day:")
    print(data["setup"])
    print(data["punchline"])
else:
    print("Failed to fetch data")