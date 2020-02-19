import unittest

from unittest.mock import call, Mock
from src.cli import Cli

class CliTest(unittest.TestCase):
    def test_log_message(self):
        cli = Cli()
        mock = Mock()
        test_string = "Hello World"

        cli.log(test_string, mock)

        mock.assert_called_once_with(test_string)
    
    def test_log_messages(self):
        cli = Cli()
        mock = Mock()
        test_strings = ["Hello", "World"]
        calls = [call("Hello"), call("World")]

        cli.log(test_strings, mock)

        mock.assert_has_calls(calls)
