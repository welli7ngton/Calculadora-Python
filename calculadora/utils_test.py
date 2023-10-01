import utils
import unittest


class CalculatorUtilsTest(unittest.TestCase):
    def test_isNumOrDot_return_bool(self):
        self.assertIn(
            utils.isNumOrDot('.'),
            [True | False],
            msg='Test Message'
        )

    def test_isValidNumber_return_bool(self):
        self.assertTrue(utils.isValidNumber('21'), 'Another message')

    def test_IsEmpty_return_object_len(self):
        self.assertIsInstance(utils.isEmpty('well'), int, 'Test')


unittest.main(verbosity=2)
