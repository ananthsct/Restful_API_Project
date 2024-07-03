import unittest
from utils import HTMLTestRunner
# import HTMLTestRunner
from tests.test_create_booking.test_create_booking import TestMethod1_Create_Booking
from tests.test_get_booking.test_get_booking import TestMethod2_Get_Booking
from tests.test_update_booking.test_update_booking import TestMethod3_Update_Booking
from datetime import datetime
from utils.payload_rfb import step_list

# Create a test suite
# def create_test_suite():
#     test_loader = unittest.TestLoader()
#     suite = unittest.TestSuite()
#     suite.addTest(test_loader.loadTestsFromTestCase(TestMethod1_Create_Booking))
#     suite.addTest(test_loader.loadTestsFromTestCase(TestMethod2_Get_Booking))
#     return suite


if __name__ == '__main__':

    today_date = str(datetime.now().date())

    test_loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    test = test_loader.suiteClass()

    test_cases = [TestMethod1_Create_Booking, TestMethod2_Get_Booking, TestMethod3_Update_Booking]
    # Loop through each test case and run them individually
    for test_case in test_cases:
        test.addTest(test_loader.loadTestsFromTestCase(test_case))
    suite.addTest(test)
    html_runner = HTMLTestRunner.HTMLTestRunner(verbosity=1, title='My unit test',
                                                description='This demonstrates the report output by HTMLTestRunner.',
                                                date=today_date)
    start_time = datetime.now()
    result = html_runner.run(suite)
    end_time = datetime.now()
    print("Step list received: ", step_list)
    print("Time taken", end_time - start_time)
    print(result)
    # Run the test suite using the TextTestRunner
    # runner = unittest.TextTestRunner()
    # runner.run(api_test_suite)
