import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from accountInfo import email, password, base_url

from core.ticketViewer import TicketViewer

import logging


def main():
    # Print account info
    print("Using email: " + email)
    print("Using url: " + base_url)

    # Kicks off the ticket viewer, which the user
    # can interact with through the command line
    ticketViewer = TicketViewer(email, password, base_url)
    ticketViewer.run()

if __name__ == "__main__":
    main()