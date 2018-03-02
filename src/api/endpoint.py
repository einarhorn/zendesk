from abc import ABCMeta, abstractmethod

import requests
from requests.auth import HTTPBasicAuth
import json
import logging

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from model.ticket import Ticket

class EndPoint(object):
    """An abstract ZenDesk API endpoint
    """

    __metaclass__ = ABCMeta

    _base_url = "https://einarhorn.zendesk.com"

    @abstractmethod
    def __init__(self, account):
        self.account = account

    @abstractmethod
    def _api_object(self):
        """"Return the model representing the specific api object"""
        pass

###########
#  GET
###########
    
    @abstractmethod
    def _get_endpoint(self):
        """"Return a string representing the specific api endpoint"""
        pass

    def get_endpoint_url(self):
        return EndPoint._base_url + self._get_endpoint()

    @abstractmethod
    def _get_key(self):
        """Return the key of the json object that we are interested in returning"""
        pass

    def get(self):
        """Return a list of all objects"""
        response = requests.get(
            self.get_endpoint_url(),
            auth=HTTPBasicAuth(self.account.email, self.account.password),
            verify=True
        )

        # For successful API call, response code will be 200 (OK)
        if(response.ok):
        # Convert content to json data
            json_data = json.loads(response.content)
            json_contents = json_data[self._get_key()]
            object_list = [self._api_object()(json_content) for json_content in json_contents]
            return object_list
        else:
        # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()
            logging.error("Received an unsuccessful response")

###########
#  GET_ID
###########

    @abstractmethod
    def _get_id_endpoint(self):
        """"Return a string representing the specific api endpoint"""
        pass
    
    def _get_id_endpoint_url(self, id):
        return EndPoint._base_url + self._get_id_endpoint().replace("{id}", str(id))

    @abstractmethod
    def _get_id_key(self):
        """Return the key of the json object that we are interested in returning"""
        pass

    def get_id(self, id):
        """Return a single object"""
        response = requests.get(
            self._get_id_endpoint_url(id),
            auth=HTTPBasicAuth(self.account.email, self.account.password),
            verify=True
        )

        # For successful API call, response code will be 200 (OK)
        if(response.ok):
        # Convert content to json data
            json_data = json.loads(response.content)
            json_content = json_data[self._get_id_key()]
            content = self._api_object()(json_content)
            return content
        else:
        # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()
            logging.error("Received an unsuccessful response")