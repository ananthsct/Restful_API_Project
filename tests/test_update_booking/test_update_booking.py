import requests
from config.config import UPDATE_BOOKING_URL
from utils.customlogger import LogGen
from tests.test_update_booking.updateBookingTestData import *
from ..conftest import create_booking
import unittest
import time


class TestMethod3_Update_Booking(unittest.TestCase):
    def test_update_booking(self):
        logger = LogGen.loggen()
        logger.info("Starting the test case for updating a booking")
        UPDATE_URL = UPDATE_BOOKING_URL + str(create_booking())
        logger.info(f"Request URL: {UPDATE_URL}")
        s_time = time.time()
        # Send a PUT request to update a booking
        response = requests.put(UPDATE_URL, json=update_booking_data(), headers=update_booking_header())
        e_time = time.time()
        response_time = float(e_time - s_time)
        print("Update_Booking_Response_Time: ", response_time)
        # Check if the response status code is 200 (OK) or 201 (Created)
        assert response.status_code in [200, 202], f"Failed to update booking. Status code: {response.status_code}"

        # Parse the response JSON
        update_response_data = response.json()
        logger.info(f"Response data: {update_response_data}")

        # Perform assertions to validate the response createBookingData
        assert update_response_data["totalprice"] == update_booking_data()["totalprice"], "Price not updated"

        logger.info("Test case for updating a booking completed")


if __name__ == "__main__":
    unittest.main()