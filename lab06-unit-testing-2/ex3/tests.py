import unittest
from unittest.mock import patch
import ex3


class TestTotal(unittest.TestCase):

    # Folosind patch context manager, implementati functia de teste pentru calculate_total. 


    def test_calculate_total(self):
        with patch('ex3.read') as mock_read:
            mock_read.return_value = [1, 2, 3]
            self.assertEqual(ex3.calculate_total('file.txt'), 6)
            mock_read.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()