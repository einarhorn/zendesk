import unittest

# For sibling directory import
import sys
from os import path
sys.path.append( path.dirname (path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from src.model.account import Account

class TestAccount(unittest.TestCase):

    def test_account_has_valid_fields(self):
        acc = Account('testEmail', 'testPass', 'testUrl')
        self.assertEqual(acc.email, 'testEmail')
        self.assertEqual(acc.password, 'testPass')
        self.assertEqual(acc.base_url, 'testUrl')

if __name__ == '__main__':
    unittest.main()