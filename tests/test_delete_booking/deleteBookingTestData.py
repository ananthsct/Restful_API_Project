from utils.authentication import get_authentication


def delete_booking_header():
    temp_token = get_authentication()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "token="+str(temp_token)
    }
    print(headers)
    return headers


if __name__ == "__main__":
    delete_booking_header()
