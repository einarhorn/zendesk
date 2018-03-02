import unittest

# For sibling directory import
import sys, os
from os import path
sys.path.append( path.dirname (path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from src.api.ticketEndpoint import TicketEndPoint
from model.ticket import Ticket
from src.model.account import Account

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from accountInfo import email, password, base_url

class TestAccount(unittest.TestCase):

    def setUp(self):
        account = Account(email, password, base_url)
        self.endpoint = TicketEndPoint(account)

    def test_has_valid_fields(self):
        self.assertEqual(self.endpoint._api_object(), Ticket)
        
        # GET fields
        self.assertEqual(self.endpoint._get_endpoint(), "/api/v2/tickets.json")
        self.assertEqual(self.endpoint._get_key(), "tickets")

        # GET_ID fields
        self.assertEqual(self.endpoint._get_id_endpoint(), "/api/v2/tickets/{id}.json")
        self.assertEqual(self.endpoint._get_id_key(), "ticket")

    def test_get_successful(self):
        get_result = self.endpoint.get()

        # Since there are > 25 entries, the API should prune to 25 entries
        self.assertEqual(len(get_result), 25)

        # Since the order is always the same, we can hardcode a test against the first entry
        first_ticket = get_result[0]
        self.assertEqual(first_ticket.id, 1)
        self.assertEqual(first_ticket.status, 'open')
        self.assertEqual(first_ticket.subject, u'Sample ticket: Meet the ticket')
    
    def test_get_next_successful(self):
        # First need to make a get() call before a get_next() call
        self.endpoint.get()

        # Verify that there are more entries that can be loaded
        self.assertTrue(self.endpoint.get_next_allowed())

        # Load next set of entries
        get_next_result = self.endpoint.get_next()

        # Since there are > 25 entries, the API should prune to 25 entries
        self.assertEqual(len(get_next_result), 25)

        # Since the order is always the same, we can hardcode a test against the first entry
        first_ticket = get_next_result[0]
        self.assertEqual(first_ticket.id, 26)
        self.assertEqual(first_ticket.status, 'open')
        self.assertEqual(first_ticket.subject, u'in labore quis mollit mollit')

    def test_get_id_successful(self):
        get_id_result = self.endpoint.get_id(1)

        # GET_ID should return a single Ticket object
        self.assertTrue(isinstance(get_id_result, Ticket))

        self.assertEqual(get_id_result.id, 1)
        self.assertEqual(get_id_result.status, 'open')
        self.assertEqual(get_id_result.subject,  u'Sample ticket: Meet the ticket')

if __name__ == '__main__':
    unittest.main()