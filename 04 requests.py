import pytest
import allure
import requests

@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This Testcase check Booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    url_get = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 200
    print("positive")

@allure.title("Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response")
@pytest.mark.positive
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 404
    print("negative")

# Yeh code RESTful API ke GET request ko PyTest aur Allure ke saath test karta hai. 
# Dono test cases API ke response ko status code ke basis par verify karte hain.
# Yeh test suite requests library se API call karta hai.
# test_get_request_positive() booking ID 1 ke liye GET request bhejta hai 
# aur check karta hai ki server ka response status code 200 aaye, jo success ko show karta hai.
# test_get_request_negative() invalid ID -1 ke saath request bhejta hai aur 
# verify karta hai ki server 404 return kare, matlab "Not Found".
# Allure ke @title aur @description se report informative hoti hai.
# Dono test PyTest ke @pytest.mark.positive se mark kiye gaye hain, lekin technically second test ek negative scenario check karta hai.
