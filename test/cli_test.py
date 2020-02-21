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

    def test_prompt_user(self):
        mock = Mock()
        expected = "A user's input"
        mock.return_value = expected
        cli = Cli(reader=mock)
        
        actual = cli.prompt_user()

        self.assertEqual(expected, actual)

    def test_prompt_user_2(self):
        mock = Mock()
        expected = "Another user's input"
        args = "Some prompt"
        mock.return_value = expected
        cli = Cli(reader=mock)

        actual = cli.prompt_user(args)
        
        mock.assert_called_once_with(args)
        self.assertEqual(expected, actual)
