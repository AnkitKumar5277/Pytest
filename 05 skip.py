import pytest
import allure
import requests
@allure.title("TC#1 - Verify that 2-2 == 0")
@allure.description("This is a BASIC Math Test")
@pytest.mark.tapas
def test_basic_math():
    assert 2-2 == 0

@allure.title("TC#2 - Verify that 3-3 is equal to 0")
@allure.description("This is a smoke Testcase which check - verify that 3-3 is equal to 0")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0


@allure.title("TC#3 - verify that 1-1 is equal to 0")
@allure.description("This is a smoke Testcase which check - verify that 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub2():
    assert 1 - 1 == 0

@pytest.mark.skip(reason="Not working,Skip it")
def test_sub3():
    assert 0 - 0 != 0

# Yeh code PyTest, Allure aur Requests libraries ka use karta hai basic subtraction test cases ke liye.
# `test_basic_math()` check karta hai `2-2 == 0`, jise `@tapas` marker diya gaya hai.
# `test_sub1()` aur `test_sub2()` regression aur smoke test cases hain jo `3-3` aur `1-1` ke liye `0` validate karte hain.
# Allure ke `@title` aur `@description` se report readable aur structured banti hai.
# `test_sub3()` ko skip kiya gaya hai with reason `"Not working"`, taaki woh test run na ho.
# Ye test cases beginners ke liye automation testing samajhne ka accha example hai.
