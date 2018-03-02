from endpoint import EndPoint
from model.ticket import Ticket

class TicketEndPoint(EndPoint):
    """A ZenDesk Ticket API endpoint
    This class extends the abstract EndPoint class, which supports the following methods:
        - get()
        - get_next_allowed()
        - get_next()
            - get_next() should only be called if get_next_allowed() returns True
        - get_id(id)
    """

    def __init__(self, account):
        """Initializes a new TicketEndPoint object for Ticket API queries

        Args:
            account (Account instance): Wrapper around Zendesk email and password

        """
        super(TicketEndPoint, self).__init__(account)

    def _api_object(self):
        """"Return a string representing the specific api endpoint"""
        return Ticket

###########
#  GET
###########

    def _get_endpoint(self):
        """"Return a string representing the specific api endpoint"""
        return "/api/v2/tickets.json"

    def _get_key(self):
        """Return the key of the json object that we are interested in returning"""
        return "tickets"

###########
#  GET_ID
###########

    def _get_id_endpoint(self):
        """"Return a string representing the specific api endpoint"""
        return "/api/v2/tickets/{id}.json"
    
    def _get_id_key(self):
        """Return the key of the json object that we are interested in returning"""
        return "ticket"