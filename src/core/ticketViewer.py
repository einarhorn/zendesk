import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from model.account import Account
from api.ticketEndpoint import TicketEndPoint
from tabulate import tabulate
import logging

class TicketViewer():
    """Handles user interaction with ticket objects in the cloud

    The user can use the methods here to request ticket objects from
    the Zendesk API.

    Currently supported API calls are GET and GET_ID.

    """

    def __init__(self, email, password, base_url):
        """Initializes a TicketViewer with the given account

        Will internally create an Account object, which will be passed around to
        the various API calls.

        Args:
            email (str): Email address of Zendesk account
            password (str): Password for Zendesk account
            base_url (str): Url of Zendesk instance

        """
        self.account = Account(email, password, base_url)
        self.endpoint = TicketEndPoint(self.account)
    
    def run(self):
        """Listens on stdin for user commands to execute

        Checks for the following inputs:
            "GET" -> "next|end"
            "GET_ID" -> "{id}"

        """
        while True:
            user_input = raw_input("Please enter a command (GET|GET_ID): ")
            if user_input == 'GET':
                self._get()
            elif user_input == 'GET_ID':
                self._get_id()
            else:
                print("Invalid input.")
    
    def _get(self):
        """Executes a GET. Will wait on user input on whether to continue paging.
        Displays 25 items per page, displaying 'id', 'subject', and 'status' for each ticket.

        If there are multiple pages, the user can input 'next' to query the next page.

        """
        # Whether to query the first page or next page
        get_first_page = True

        while True:
            # Query API for list of Ticket objects
            if get_first_page:
                ticket_list = self.endpoint.get()
            else:
                ticket_list = self.endpoint.get_next()

            # If API call was unsuccessful, return to main menu
            if ticket_list == []:
                print("No data returned")
                break

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
            print

            # Print if more info to display
            if self.endpoint.get_next_allowed():
                user_input = raw_input("Type 'next' to see next page, 'end' to return to menu: ")
                print

                if user_input == 'next':
                    get_first_page = False
                    continue
                else:
                    break
            else:
                print("No more tickets to display")
                break

    def _get_id(self):
        """Executes a GET_ID. Will request an ID from the user.
        
        Invalid query will return a None ticket from the endpoint class.

        Displays 'id', 'subject', 'status', and 'description' for each ticket.

        """
        # Request id from user
        id = raw_input("Please enter an id: ")
        
        # Check if id is valid positive integer
        if not id.isdigit():
            logging.error("Input is not a valid id")
            return

        # Query API for ticket
        ticket = self.endpoint.get_id(id)

        # Handle invalid id / invalid query
        if not ticket:
            print("Unable to find ticket.")
            return

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
        print