import requests
import json
from config.config import BASE_URL
from dotenv import load_dotenv
import os
load_dotenv()


def get_authentication():
    url = f"{BASE_URL}/auth"

    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "username": os.getenv("user"),
        "password": os.getenv("password")
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response_data = response.json()
        auth_token = response_data["token"]
        assert response.status_code == 200
        print(auth_token)
        return auth_token
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")


if __name__ == "__main__":
    get_authentication()
