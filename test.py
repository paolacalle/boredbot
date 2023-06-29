import unittest
import requests
from unittest.mock import patch #https://docs.python.org/3/library/unittest.mock.html
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

        mock_input.assert_has_calls([unittest.mock.call(), unittest.mock.call()])


    @patch('builtins.input', side_effect=['0', '1'])
    def test_get_price_range_vaild_input(self, mock_input):
        expected = 'minprice=0&maxprice=1'

        with patch ('sys.stdout', new=StringIO()) as mock_stdout:
            result = get_price_range()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 2)
        mock_input.assert_has_calls([unittest.mock.call(), unittest.mock.call()])


    @patch('builtins.input', side_effect=['100','0','-1','1'])
    def test_get_price_range_invaild_then_vaild_input(self, mock_input): 
        expected = 'minprice=0&maxprice=1'

        with patch ('sys.stdout', new=StringIO()) as mock_stdout: 
            result = get_price_range()
            output = mock_stdout.getvalue().strip()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 4)
        mock_input.assert_has_calls([unittest.mock.call(), unittest.mock.call(), unittest.mock.call(), unittest.mock.call()])

    

if __name__ == '__main__':
    unittest.main()




# def test_price_range(self):
#     self.assertEqual(get_price_range(selectedMin='0', selectedMax='1'),'minprice=0&maxprice=1')
#     capturingOutput = StringIO()
#     sys.stdout = capturingOutput
#     get_price_range(selectedMin='2', selectedMax='4')
#     printingOutput = capturingOutput.getvalue().strip()
    
#     self.assertEqual(printingOutput, 'Invaild Input, range is 0-1.')


# def test_get_accessibility(self):
#     self.assertEqual(get_accessibility(response='1'),'accessibility=1')


# def test_get_participants(self):
#     self.assertEqual(get_participants(response='2'),'participants=2')


# def test_get_opinion(self):
#     self.assertEqual(get_opinion(response='yessir'), True)


# def test_stay_switch(self):
#     self.assertEqual(stay_switch(response='yessir'), 'Invalid input.')

