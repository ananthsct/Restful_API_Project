import pytest
import requests
from config.config import CREATE_BOOKING_URL, UPDATE_BOOKING_URL
from utils.customlogger import LogGen
from tests.test_update_booking.updateBookingTestData import *


@pytest.fixture()
# Test case for creating a booking
def test_create_booking():
    logger = LogGen.loggen()
    logger.info("Starting the test case for updating a booking")
    logger.info(f"Request URL: {CREATE_BOOKING_URL}")

    # Send a POST request to create a booking
    response = requests.post(CREATE_BOOKING_URL, json=create_booking_data(), headers=create_booking_header())

    # Parse the response JSON
    booking_response_data = response.json()

    booking_id = booking_response_data["bookingid"]
    logger.info(f"Booking created with ID: {booking_id}")
    logger.info("Test case for creating a booking completed")
    return booking_id


def test_update_booking(test_create_booking):
    logger = LogGen.loggen()
    logger.info("Starting the test case for updating a booking")
    UPDATE_URL = UPDATE_BOOKING_URL + str(test_create_booking)
    logger.info(f"Request URL: {UPDATE_URL}")

    # Send a PUT request to update a booking
    response = requests.put(UPDATE_URL, json=update_booking_data(), headers=update_booking_header())

    # Check if the response status code is 200 (OK) or 201 (Created)
    assert response.status_code in [200, 202], f"Failed to update booking. Status code: {response.status_code}"

    # Parse the response JSON
    update_response_data = response.json()
    logger.info(f"Response data: {update_response_data}")

    # Perform assertions to validate the response createBookingData
    assert update_response_data["totalprice"] == update_booking_data()["totalprice"], "Price not updated"

    logger.info("Test case for updating a booking completed")
