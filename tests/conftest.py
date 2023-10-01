import pytest
import requests
from config.config import *
from utils.customlogger import LogGen
from tests.test_create_booking.createBookingTestData import create_booking_data, create_booking_header


@pytest.fixture
# Test case for creating a booking
def create_booking():
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


if __name__ == "__main__":
    create_booking()
