import requests

# Define the URL you want to send the request to
url = "https://httpbin.org/headers"

# Custom headers dictionary
headers = {
    "User-Agent": "MyApp/1.0",
    "Accept": "application/json",
    "X-Custom-Header": "CustomValue"
}

# Send GET request with headers
response = requests.get(url, headers=headers)

# Print the response in JSON format to see what headers the server received
print("Response Headers Received by Server:")
print(response.json())
