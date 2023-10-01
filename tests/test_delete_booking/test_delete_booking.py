import pytest
import requests
from config.config import CREATE_BOOKING_URL, DELETE_BOOKING_URL
from utils.customlogger import LogGen
from tests.test_delete_booking.deleteBookingTestData import *


@pytest.fixture()
# Test case for creating a booking
def test_create_booking():
    logger = LogGen.loggen()
    logger.info("Starting the test case for creating a booking")
    logger.info(f"Request URL: {CREATE_BOOKING_URL}")

    # Send a POST request to create a booking
    response = requests.post(CREATE_BOOKING_URL, json=create_booking_data(), headers=create_booking_header())

    # Parse the response JSON
    booking_response_data = response.json()

    booking_id = booking_response_data["bookingid"]
    logger.info(f"Booking created with ID: {booking_id}")
    logger.info("Test case for creating a booking completed")
    return booking_id


def test_delete_booking(test_create_booking):
    logger = LogGen.loggen()
    logger.info("Starting the test case for deleting a booking")
    DELETE_URL = DELETE_BOOKING_URL + str(test_create_booking)
    logger.info(f"Request URL: {DELETE_URL}")

    # Send a PUT request to update a booking
    response = requests.delete(DELETE_URL, headers=delete_booking_header())

    # Check if the response status code is 201 for deleting content as per restful document
    assert response.status_code == 201, f"Failed to update booking. Status code: {response.status_code}"

    logger.info("Test case for deleting a booking completed")
