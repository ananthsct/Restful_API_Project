def create_booking_data():
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
    return payload


def create_booking_header():
    headers = {
        "Content-Type": "application/json"
    }
    return headers
