import requests

## A simple function to fetch data from a public API and print the results.
def fetch_api_data():
    url = "https://jsonplaceholder.typicode.com"

    response = requests.get(f"{url}/posts")
    if response.status_code == 200:
        data = response.json()
        print("API data fetched successfully")
        return data
    else:
        print("Failed to fetch API data")
        return None


if __name__ == "__main__":
    api_data = fetch_api_data()

    ## Print the first 5 posts from the API data
    for post in api_data[:5]:
        print(f"Post ID: {post['id']}, Title: {post['title']}")

    