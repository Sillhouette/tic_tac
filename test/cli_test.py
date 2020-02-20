import unittest

from unittest.mock import call, Mock
from src.cli import Cli

class CliTest(unittest.TestCase):
    def test_log_message(self):
        mock = Mock()
        cli = Cli(mock)
        test_string = "Hello World"

        cli.log(test_string)

        mock.assert_called_once_with(test_string)
    
    def test_log_messages(self):
        mock = Mock()
        cli = Cli(mock)
        test_strings = ["Hello", "World"]
        calls = [call("Hello"), call("World")]

        cli.log(test_strings)

        mock.assert_has_calls(calls)
