import unittest

# For sibling directory import
import sys, os
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.ticketEndpoint import TicketEndPoint
from src.ticket import Ticket
from src.account import Account

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from accountInfo import email, password

class TestAccount(unittest.TestCase):

    def setUp(self):
        account = Account(email, password)
        self.endpoint = TicketEndPoint(account)

    def test_has_valid_fields(self):
        self.assertEqual(self.endpoint.api_endpoint(), "/api/v2/tickets.json")
        self.assertEqual(self.endpoint.api_object(), Ticket)

if __name__ == '__main__':
    unittest.main()