import unittest
import requests
from unittest.mock import patch
from io import StringIO
import sys
from bored import get_type, get_price_range, get_accessibility, get_participants, get_opinion, stay_switch


class unit_test(unittest.TestCase):

    @patch('builtins.input', side_effect=['education'])
    def test_get_type_vaild_input(self, mock_input):
        expected = 'type=education'

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_type()

        self.assertEqual(result, expected)
        mock_input.assert_called_once_with()

    @patch('builtins.input', side_effect=['invalid', 'education'])
    def test_get_type_invalid_input_then_valid_input(self, mock_input):
        expected = 'type=education'

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_type()
            output = mock_stdout.getvalue().strip()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 2)
        mock_input.assert_has_calls(
            [unittest.mock.call(), unittest.mock.call()])

    @patch('builtins.input', side_effect=['0', '1'])
    def test_get_price_range_vaild_input(self, mock_input):
        expected = 'minprice=0&maxprice=1'

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_price_range()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 2)
        mock_input.assert_has_calls(
            [unittest.mock.call(), unittest.mock.call()])

    @patch('builtins.input', side_effect=['100', '0', '-1', '1'])
    def test_get_price_range_invaild_then_vaild_input(self, mock_input):
        expected = 'minprice=0&maxprice=1'

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_price_range()
            output = mock_stdout.getvalue().strip()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 4)
        mock_input.assert_has_calls([unittest.mock.call(
        ), unittest.mock.call(), unittest.mock.call(), unittest.mock.call()])

    @patch('builtins.input', side_effect=['1'])
    def test_get_accessibility_valid_input(self, mock_input):
        expected = 'accessibility=1'

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_accessibility()

        self.assertEqual(result, expected)
        mock_input.assert_called_once_with()

    @patch('builtins.input', side_effect=['2', '0'])
    def test_get_accessibility_invalid_then_valid_input(self, mock_input):
        expected = 'accessibility=0'

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_accessibility()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 2)
        mock_input.assert_has_calls(
            [unittest.mock.call(), unittest.mock.call()])

    @patch('builtins.input', side_effect=['2'])
    def test_get_participants_valid_input(self, mock_input):
        expected = 'participants=2'

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_participants()

        self.assertEqual(result, expected)
        mock_input.assert_called_once_with()

    @patch('builtins.input', side_effect=['0', '1'])
    def test_get_participants_invalid_then_valid_input(self, mock_input):
        expected = 'participants=1'

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_participants()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 2)
        mock_input.assert_has_calls(
            [unittest.mock.call(), unittest.mock.call()])

    @patch('builtins.input', side_effect=['yes'])
    def test_get_opinion_valid_input(self, mock_input):
        expected = False

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_opinion()

        self.assertEqual(result, expected)
        mock_input.assert_called_once_with()

    @patch('builtins.input', side_effect=['silly', 'no'])
    def test_get_opinion_invalid_then_valid_input(self, mock_input):
        expected = True

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_opinion()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 2)
        mock_input.assert_has_calls(
            [unittest.mock.call(), unittest.mock.call()])

    @patch('builtins.input', side_effect=['switch'])
    def test_stay_switch_valid(self, mock_input):
        expected = True

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = stay_switch()

        self.assertEqual(result, expected)
        mock_input.assert_called_once_with()

    @patch('builtins.input', side_effect=['BREAK', 'stay'])
    def test_stay_switch_invalid_then_valid_input(self, mock_input):
        expected = False

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = stay_switch()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 2)
        mock_input.assert_has_calls(
            [unittest.mock.call(), unittest.mock.call()])


if __name__ == '__main__':
    unittest.main()
