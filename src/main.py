from core.ticketViewer import TicketViewer

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from accountInfo import email, password

def main():
    # Kicks off the ticket viewer, which the user
    # can interact with through the command line
    ticketViewer = TicketViewer(email, password)
    ticketViewer.run()

if __name__ == "__main__":
    main()