from endpoint import EndPoint
from ..model.ticket import Ticket

class TicketEndPoint(EndPoint):
    def __init__(self, account):
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