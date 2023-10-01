import requests
from config.config import DELETE_BOOKING_URL
from utils.customlogger import LogGen
from tests.test_delete_booking.deleteBookingTestData import *
from ..conftest import create_booking


def test_delete_booking(create_booking):
    logger = LogGen.loggen()
    logger.info("Starting the test case for deleting a booking")
    DELETE_URL = DELETE_BOOKING_URL + str(create_booking)
    logger.info(f"Request URL: {DELETE_URL}")

    # Send a PUT request to update a booking
    response = requests.delete(DELETE_URL, headers=delete_booking_header())

    # Check if the response status code is 201 for deleting content as per restful document
    assert response.status_code == 201, f"Failed to update booking. Status code: {response.status_code}"

    logger.info("Test case for deleting a booking completed")
