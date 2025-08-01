import pytest
import allure
import requests

# Create Token - POST
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}

def test_create_token():
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)
    assert type(token) == str
    assert len(token) > 0

# Yeh code RESTful Booker API ke /auth endpoint ko test karta hai 
# jisme ek token generate kiya jata hai using valid username and password. 
# Yeh test case test_create_token() RESTful API ke /auth endpoint par POST request bhejta hai 
# jisme "username": "admin" aur "password": "password123" diya gaya hai. Agar credentials valid hote hain, 
# toh API ek authentication token return karti hai.
# Test verify karta hai ki:
# Status code 200 ho (successful authentication).
# Response ke andar "token" key ho.
# Token ek non-empty string ho.
# type(token) string ho aur len(token) > 0.
# Yeh token future mein authorized requests (like create, update, delete booking) ke liye use kiya ja sakta hai.
# Aap Allure decorators (@allure.title, @allure.description) bhi use kar sakte ho is report ko aur informative banane ke liye.

