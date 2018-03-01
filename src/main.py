#main.py

# Classes
# -MiniTicket?
# -Ticket
#   -Load()
#   -PrintLarge()
#   -PrintSmall()
# -EndPoint (Abstract)
#   -TicketEndPoint
#       -GET()
#       -GET_ID()

import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from accountInfo import email, password
from account import Account
from ticketEndpoint import TicketEndPoint


def main():
    account = Account(email, password)
    endpoint = TicketEndPoint(account)
    (endpoint.get())
    endpoint.get_id(1)

main()