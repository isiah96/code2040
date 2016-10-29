import requests
import json
from datetime import datetime, timedelta

'''
' Step 5
' add_to_date() - Retrieves a dictionary from the server containing datestamp -
' a string (formatted as an ISO 8601 datestamp), and interval - an integer
' (representing the amount of seconds that the datestamp should be incremented
' by), adds interval to the represented date, and sends it back to the server
' for validation.
'''

def add_to_date():
    token = '5ea5ad07f90d2f12f2b36cd9e48c01ab'
    link_dating = "http://challenge.code2040.org/api/dating"
    link_validate = "http://challenge.code2040.org/api/dating/validate"

    r = requests.post(link_dating, json = {'token': token})
    pack = json.loads(r.text)

    datestamp = pack['datestamp']
    interval = pack['interval']

    #convert string to a datetime object for easy incrementing
    date_obj = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')
    new_date_obj = date_obj + timedelta(seconds = interval)

    #convert datetime object back to string
    new_date = new_date_obj.strftime('%Y-%m-%dT%H:%M:%SZ')

    r = requests.post(link_validate, json = {'token': token, 'datestamp': new_date})
    print(r.text)

add_to_date()
