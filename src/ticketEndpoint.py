from endpoint import EndPoint

class TicketEndPoint(EndPoint):
    def api_endpoint(self):
        """"Return a string representing the specific api endpoint"""
        return "/api/v2/tickets.json"
    
    def api_obejct(self):
        return -1