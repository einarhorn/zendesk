import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from model.account import Account
from api.ticketEndpoint import TicketEndPoint
from tabulate import tabulate

class TicketViewer():
    """Handles user interaction with ticket objects in the cloud

    The user can use the methods here to request ticket objects from
    the Zendesk API.

    Currently supported API calls are GET and GET_ID.

    """

    def __init__(self, email, password):
        """Initializes a TicketViewer with the given email and password

        Will internally create an Account object, which will be passed around to
        the various API calls.

        Args:
            email (str): Email address of Zendesk account
            password (str): Password for Zendesk account

        """
        self.account = Account(email, password)
        self.endpoint = TicketEndPoint(self.account)
    
    def run(self):
        """Listens on stdin for user commands to execute

        Checks for the following inputs:
            "get"
            "get_id" -> "{id}"


        """
        while True:
            user_input = raw_input("Please enter a command:\n")
            if user_input == 'get':
                self._get()
            elif user_input == 'get_id':
                self._get_id()
    
    def _get(self):
        # Query API for list of Ticket objects
        ticket_list = self.endpoint.get()

        # List of headers to display
        headers = ['id', 'subject', 'status']
        
        # Get header items from ticket
        tickets_as_list = [ticket.get_ticket_as_list(headers) for ticket in ticket_list]

        # Create table
        tabulation = tabulate(
            tickets_as_list,
            headers=headers
        )

        # Display table
        print(tabulation)

    def _get_id(self):
        id = raw_input("Please enter an id:\n")
        # TODO: Check if id is int

        # Query API for ticket
        ticket = self.endpoint.get_id(id)

        # List of headers to display
        headers = ['id', 'subject', 'status', 'description']
        
        # Get header items from ticket
        ticket_as_list = ticket.get_ticket_as_list(headers)

        # Create table
        tabulation = tabulate(
            [ticket_as_list],
            headers=headers
        )

        # Display table
        print(tabulation)