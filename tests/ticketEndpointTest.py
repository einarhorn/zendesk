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
        self.assertEqual(self.endpoint._api_object(), Ticket)
        
        # GET fields
        self.assertEqual(self.endpoint._get_endpoint(), "/api/v2/tickets.json")
        self.assertEqual(self.endpoint._get_key(), "tickets")

        # GET_ID fields
        self.assertEqual(self.endpoint._get_id_endpoint(), "/api/v2/tickets.json")
        self.assertEqual(self.endpoint._get_id_key(), "ticket")

    def test_get_successful(self):
        get_result = self.endpoint.get()

        # Since there are > 25 entries, the API should prune to 25 entries
        self.assertEqual(len(get_result), 25)


    
    def test_get_id_successful(self):
        get_id_result = self.endpoint.get_id(1)

        # GET_ID should return a single Ticket object
        self.assertTrue(isinstance(get_id_result, Ticket))

if __name__ == '__main__':
    unittest.main()