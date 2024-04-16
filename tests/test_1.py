import requests

url = "https://restful-booker.herokuapp.com/booking"
headers = {
        "Content-Type": "application/json"
    }
payload = {
        "firstname": "Ananth",
        "lastname": "kamaraj",
        "totalprice": 432,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-01"
        },
        "additionalneeds": "Lunch"
    }
response = requests.post(url, json=payload, headers=headers)
status_code = response.status_code
print(status_code)
