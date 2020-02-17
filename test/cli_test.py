import unittest

from src.cli import Cli

class CliTest(unittest.TestCase):
    def test_answer(self):
        cli = Cli()
        self.assertEqual(5, cli.func(4))
