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

    This class needs to be extended by endpoint specific classes. The following
    methods need to be implemented:
        _api_object()
        _get_endpoint()
        _get_key()
        _get_id_endpoint()
        _get_id_key()
    
    Currently only GET and GET_ID API calls are supported.

    Explanation of GET paging:
        get_next() can only be called if get() has been called once.
        get_next() can be called iteratively as long as there are pages left to be queried.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, account):
        self.account = account
        self.get_next_url = None

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

    @abstractmethod
    def _get_key(self):
        """Return the key of the json object that we are interested in returning"""
        pass

    def get_endpoint_url(self, per_page=25):
        """Return the full endpoint url to query for the GET request
        
        Args:
            per_page (int): Number of entries to return per GET query
        
        """
        return self.account.base_url + self._get_endpoint() + "?per_page=" + str(per_page)

    def get_next_allowed(self):
        """Returns whether a get_next() call is allowed. This only happens when a user has made
        a get() call, and the request indicated that there more pages to be queried.
        
        """
        return self.get_next_url != None
    
    def get(self):
        """A GET call to the endpoint. Will return a list of model objects"""
        return self._get()

    def get_next(self):
        """A GET call to the endpoint. Will return a list of the next available page of objects"""
        if (self.get_next_allowed()):
            return self._get(self.get_next_url)
        else:
            logging.error("No next page")
            return []

    def _get(self, url=None):
        """Return a list of all objects"""
        if url is None:
            url = self.get_endpoint_url()
        response = self._generate_get_request(url)

        # If request could not be made, response is None
        if response is None:
            return []

        # For successful API call, response code will be 200 (OK)
        if(response.ok):
            # Convert content to json data
            json_data = json.loads(response.content)

            # Check if there is a next page
            if 'next_page' in json_data:
                self.get_next_url = json_data['next_page']
            else:
                self.get_next_url = None

            # Extract main content
            json_contents = json_data[self._get_key()]
            object_list = [self._api_object()(json_content) for json_content in json_contents]
            return object_list
        else:
            # If response code is not ok (200), print the resulting http error code with description
            self._generate_bad_response_error(url, response)
            return []
    
###########
#  GET_ID
###########

    @abstractmethod
    def _get_id_endpoint(self):
        """"Return a string representing the specific api endpoint"""
        pass
    
    @abstractmethod
    def _get_id_key(self):
        """Return the key of the json object that we are interested in returning"""
        pass

    def _get_id_endpoint_url(self, id):
        """Return the full endpoint url to query for the GET_ID request"""
        return self.account.base_url + self._get_id_endpoint().replace("{id}", str(id))

    def get_id(self, id):
        """Return a single object"""
        url = self._get_id_endpoint_url(id)
        response = self._generate_get_request(url)

        # If request could not be made, response is None
        if response is None:
            return []

        # For successful API call, response code will be 200 (OK)
        if(response.ok):
            # Convert content to json data
            json_data = json.loads(response.content)
            json_content = json_data[self._get_id_key()]
            content = self._api_object()(json_content)
            return content
        else:
            # If response code is not ok (200), print the resulting http error code with description
            self._generate_bad_response_error(url, response)
            return None

###########
#  GET HELPERS
###########

    def _generate_get_request(self, url):
        """Generate a GET request using requests library"""
        try:
            request = requests.get(
                url,
                auth=HTTPBasicAuth(self.account.email, self.account.password),
                verify=True
            )
            return request
        except Exception:
            print("Unknown exception occured. Check your internet connection?")
            return None
        
    def _generate_bad_response_error(self,url,response):
        """Print out details of the bad response"""
        error_string = "Attempted to query " \
                        + url \
                        + ". Received an unsuccessful response (" \
                        + str(response.status_code) \
                        + ")."
        logging.error(error_string)