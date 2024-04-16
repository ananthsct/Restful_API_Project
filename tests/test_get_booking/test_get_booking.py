import requests
import unittest
from config.config import GET_BOOKING_URL
from utils.customlogger import LogGen
from tests.test_get_booking.getBookingTestData import *
from ..conftest import create_booking
import time


class TestMethod2_Get_Booking(unittest.TestCase):
    def test_get_booking(self):
        logger = LogGen.loggen()
        logger.info("Starting the test case for getting a booking")
        GET_URL = GET_BOOKING_URL + str(create_booking())
        logger.info(f"Request URL: {GET_URL}")
        s_time = time.time()
        # Send a GET request to get a booking
        response = requests.get(GET_URL, headers=get_booking_header())
        e_time = time.time()
        response_time = float(e_time - s_time)
        print("Get_Booking_Response_Time: ", response_time)
        get_booking_response_data = response.json()
        logger.info(f"Response data: {get_booking_response_data}")
        print("Booking_response :", get_booking_response_data)

        # Check if the response status code is 200 for getting content as per restful document
        assert response.status_code == 200, f"Failed to update booking. Status code: {response.status_code}"

        logger.info("Test case for deleting a getting completed")


if __name__ == "__main__":
    unittest.main()