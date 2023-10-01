from utils.authentication import get_authentication


def create_booking_data():
    # In future you can replace this from the excel or JSON
    payload = {
        "firstname": "Ananth",
        "lastname": "kamaraj",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-09-30",
            "checkout": "2022-10-01"
        },
        "additionalneeds": "Lunch"
    }
    return payload


def update_booking_data():
    # In future you can replace this from the excel or JSON
    payload = {
        "firstname": "Ananth",
        "lastname": "kamaraj",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-09-30",
            "checkout": "2022-10-01"
        },
        "additionalneeds": "Lunch"
    }
    return payload


def create_booking_header():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def update_booking_header():
    temp_token = get_authentication()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "token="+str(temp_token)
    }
    print(headers)
    return headers


if __name__ == "__main__":
    update_booking_header()
