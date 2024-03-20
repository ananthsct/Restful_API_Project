import unittest
from utils import HTMLTestRunner
from tests.test_create_booking.test_create_booking import TestMethod1_Create_Booking
from tests.test_get_booking.test_get_booking import TestMethod2_Get_Booking
from datetime import datetime


# Create a test suite
def create_test_suite():
    test_loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(test_loader.loadTestsFromTestCase(TestMethod1_Create_Booking))
    suite.addTest(test_loader.loadTestsFromTestCase(TestMethod2_Get_Booking))
    return suite


if __name__ == '__main__':
    # Specify the file name for the HTML report
    report_file = 'reports/my_report5.html'
    today_date = str(datetime.now().date())
    # Use open() to create a file object in Python 3
    with open(report_file, 'wb') as fp:
        # Create a test runner with HtmlTestRunner
        runner = unittest.TextTestRunner()
        html_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='My unit test',
                                                    description='This demonstrates the report output by HTMLTestRunner.',
                                                    date=today_date)

        # Run the test suite using the chosen runner
        api_test_suite = create_test_suite()
        html_runner.run(api_test_suite)
