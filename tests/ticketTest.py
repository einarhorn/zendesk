import unittest

# For sibling directory import
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.ticket import Ticket

class TestTicket(unittest.TestCase):

    def test_ticket_has_valid_fields(self):
        ticket = Ticket()
        self.assertEqual(ticket.id, 0)

if __name__ == '__main__':
    unittest.main()