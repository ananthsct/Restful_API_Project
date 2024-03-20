import unittest
import time
from utils import HTMLTestRunner


class CustomHTMLTestRunner(HTMLTestRunner):
    def generate_report(self, test_results, **kwargs):
        report = super().generate_report(test_results, **kwargs)
        # Iterate through each test result
        for test_result in test_results:
            # Calculate test case execution time
            test_duration = test_result['stop_time'] - test_result['start_time']
            # Add test case execution time to the report
            report += f"<p>Test: {test_result['name']} - Duration: {test_duration:.6f} seconds</p>\n"
        return report


class TestExample(unittest.TestCase):

    def test_addition(self):
        time.sleep(1)  # Simulate some time-consuming operation
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        time.sleep(0.5)  # Simulate some time-consuming operation
        self.assertEqual(3 - 1, 2)


if __name__ == '__main__':
    # Load test cases
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestExample)

    # Create a test suite
    test_suite = unittest.TestSuite(test_cases)

    # Define the output file path
    output_file = 'reports/my_report5.html'

    # Open the output file to write the test results
    with open(output_file, 'w') as report_file:
        # Initialize CustomHTMLTestRunner
        runner = CustomHTMLTestRunner(
            stream=report_file,
            title='Unit Test Report',
            description='Basic Test Report'
        )
        # Run the test suite
        runner.run(test_suite)
