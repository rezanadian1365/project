# API
# API for the project
# This file contains the API for the project. It is used to get the data from the database and send it to the frontend.
# It is also used to get the data from the frontend and send it to the database.
import requests

# url = "https://reqres.in/api/users"
# data = {"name": "Reza", "age": 38, "email": "ir@gmail.com"}
url = "https://reqres.in/api/login"
login_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
url = "https://reqres.in/api/login"
response = requests.post(url, json=login_data)
if response.status_code == 201:
    print("data sent successfully")
    print(response.json())
    print(response.status_code)
elif response.status_code == 400:  # Bad Request
    print("data not sent")
    print(response.json())
    print(response.status_code)
else:
    print("data not sent")
    print(response.status_code)
