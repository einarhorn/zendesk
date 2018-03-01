from abc import ABCMeta, abstractmethod

import requests
from requests.auth import HTTPBasicAuth
import json

class EndPoint(object):
    """An abstract ZenDesk API endpoint
    """

    __metaclass__ = ABCMeta

    base_url = "https://einarhorn.zendesk.com"

    @abstractmethod
    def __init__(self, account):
        self.account = account

    def get_endpoint_url(self):
        return EndPoint.base_url + self.api_endpoint()

    def get(self):
        """Return the sale price for this vehicle as a float amount."""
        response = requests.get(
            self.get_endpoint_url(),
            auth=HTTPBasicAuth(self.account.email, self.account.password),
            verify=True
        )

        # For successful API call, response code will be 200 (OK)
        if(response.ok):
        # Convert content to json data
            json_data = json.loads(response.content)
            return json_data
        else:
        # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()
            print("ERR")

    @abstractmethod
    def api_endpoint(self):
        """"Return a string representing the specific api endpoint"""
        pass
    
    @abstractmethod
    def api_obejct(self):
        pass