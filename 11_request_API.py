# pip install requests
# Install the 'requests' package/library if it is not already installed.

import requests  # Import the requests library to make HTTP/API requests


# Send a GET request to the API URL
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# Check the HTTP response status code
# 200 means the request was successful and the server returned a response
print(response.status_code)

# Convert the JSON response into a Python object (usually a dictionary)
data = response.json()

# Print the data received from the API
print(data)