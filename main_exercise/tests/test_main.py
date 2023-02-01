import importlib
import json
import os
import unittest
from unittest.mock import patch

from input_manager import InputManager
from rest_client import RestClient
import tests.testutils as testutils

TEST_VARIANTS_DIR = "test_cases"
MOCK_INPUT_FILE_PATH = "mock_config.json"
MAIN_MODULE = "main"

method_to_test = getattr(importlib.import_module(MAIN_MODULE), "calculate_dividend_tax")


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data = self.test_case_data[
            testutils.strip_test_prefix(self._testMethodName)]

        self._patch_input_manager()
        self._patch_rest_client()

        self.mock_input_manager.load_input.return_value = self.test_data.input
        rest_client_instance = self.mock_rest_client.return_value
        self.mock_get_rates_fun = \
            rest_client_instance.get_currency_rate_from_previous_working_day
        self.mock_get_rates_fun.side_effect = self.test_data.rates

    def _patch_rest_client(self):
        self.rest_client_patcher = patch(f"{MAIN_MODULE}.RestClient")
        self.mock_rest_client = self.rest_client_patcher.start()
        self.mock_rest_client.mock_add_spec(RestClient)

        self.addCleanup(self.rest_client_patcher.stop)

    def _patch_input_manager(self):
        self.input_manager_patcher = patch(f"{MAIN_MODULE}.InputManager")
        self.mock_input_manager = self.input_manager_patcher.start()
        self.mock_input_manager.mock_add_spec(InputManager)

        self.addCleanup(self.input_manager_patcher.stop)

    def _test_body(self):
        output = method_to_test(MOCK_INPUT_FILE_PATH)

        self.mock_input_manager.load_input.assert_called_once_with(MOCK_INPUT_FILE_PATH)
        self.mock_rest_client.assert_called_once_with(self.test_data.input.currency)

        self.assertEqual(self.mock_get_rates_fun.call_count,
                         len(self.test_data.input.dates))
        get_rates_calls = self.mock_get_rates_fun.call_args_list
        for call_no in range(len(get_rates_calls)):
            self.assertEqual(get_rates_calls[call_no].args[0],
                             self.test_data.input.dates[call_no].date)

        self.assertDictEqual(self.test_data.expected_output.dict(), output.dict())


def register_test_cases():
    """Register test functions for unittest

    This function reads test configuration for the given test case from JSON config file
    located in 'test_cases' directory. Each entry of such JSON is of type 'TestData'
    defined in 'testutils' module.
    After reading the configuration, function registers test functions in the given
    TestCase class. Thanks to that they will be caught by unittest and run.
    """
    test_case_config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        TEST_VARIANTS_DIR,
        f"{testutils.strip_test_prefix(__name__.split('.')[-1])}.json"
    )
    with open(test_case_config_file, 'r') as file_handler:
        setattr(TestMain, "test_case_data", dict(json.loads(file_handler.read())))

    test_case_data = getattr(TestMain, "test_case_data")
    for test_case in test_case_data:
        test_case_data[test_case] = testutils.TestData(**test_case_data[test_case])
        setattr(TestMain, f"test_{test_case}", TestMain._test_body)


register_test_cases()
