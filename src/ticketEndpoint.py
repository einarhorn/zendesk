from endpoint import EndPoint
from ticket import Ticket

class TicketEndPoint(EndPoint):
    def __init__(self, account):
        super(TicketEndPoint, self).__init__(account)

    def api_endpoint(self):
        """"Return a string representing the specific api endpoint"""
        return "/api/v2/tickets.json"
    
    def api_object(self):
        return Ticket