import unittest
import requests
from config.config import CREATE_BOOKING_URL
from utils.customlogger import LogGen
from tests.test_create_booking.createBookingTestData import create_booking_data, create_booking_header
import time
import logging


# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Test case for creating a booking
class TestMethod1_Create_Booking(unittest.TestCase):
    def test_create_booking(self):
        # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = LogGen.loggen()
        logger.info("Starting the test case for creating a booking")
        logger.info(f"Request URL: {CREATE_BOOKING_URL}")
        s_time = time.time()
        # Send a POST request to create a booking
        response = requests.post(CREATE_BOOKING_URL, json=create_booking_data(), headers=create_booking_header())
        e_time = time.time()
        response_time = float(e_time - s_time)
        print("Create_Booking_Response_Time: ", response_time)
        logger.info(f"Response_Time: {response_time}")
        # Check if the response status code is 200 (OK) or 201 (Created)
        assert response.status_code in [300, 201], f"Failed to create booking. Status code: {response.status_code}"

        # Parse the response JSON
        booking_response_data = response.json()
        logger.info(f"Response data: {booking_response_data}")

        # Perform assertions to validate the response createBookingData
        assert "bookingid" in booking_response_data, "Booking ID not found in response"
        assert booking_response_data["booking"]["firstname"] == create_booking_data()["firstname"], "First name mismatch"
        assert booking_response_data["booking"]["lastname"] == create_booking_data()["lastname"], "Last name mismatch"

        booking_id = booking_response_data["bookingid"]
        logger.info(f"Booking created with ID: {booking_id}")
        print(f"Booking created with ID: {booking_id}")
        logger.info("Test case for creating a booking completed")

    def test_sample(self):
        print("Sample test case")
        time.sleep(1)
        print("sample test ends")


if __name__ == "__main__":
    unittest.main()
