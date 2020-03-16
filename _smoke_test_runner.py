import unittest

from test.three_by_three_hard_strategy_smoke_test import ThreeByThreeHardStrategySmokeTest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ThreeByThreeHardStrategySmokeTest))

    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Note: run the tests from the command line with:
# 'python3 -m unittest _test_runner.py -v'
