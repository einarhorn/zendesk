#main.py

import requests
from requests.auth import HTTPBasicAuth
import json


def get_account_info():
    from account import email, password
    return email, password


def generate_endpoint_url():
    # GET /api/v2/tickets.json
    base_url = "https://einarhorn.zendesk.com"
    ticket_endpoint = "/api/v2/tickets.json"
    ticket_full_endpoint = base_url + ticket_endpoint
    return ticket_full_endpoint



def query_endpoint(url, email, password):
    response = requests.get(url, auth=HTTPBasicAuth(email, password), verify=True)

    # For successful API call, response code will be 200 (OK)
    if(response.ok):
       # Convert content to json data
        json_data = json.loads(myResponse.content)
        for key in json_data:
            print key
    else:
    # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()
        print("ERR")


def main():
    email, password = get_account_info()
    url = generate_endpoint_url()
    query_endpoint(url, email, password)



main()