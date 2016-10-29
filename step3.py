import requests
import json

'''
' Step 3
' find_needle() - Retrieves a dictionary from the server containing
' needle - a string, and haystack - an array of strings, identifies the index
' of needle in haystack, then sends it back for validation.
'''

def find_needle():
    token = '5ea5ad07f90d2f12f2b36cd9e48c01ab'
    link_haystack = "http://challenge.code2040.org/api/haystack"
    link_validate = "http://challenge.code2040.org/api/haystack/validate"

    r = requests.post(link_haystack, json = {'token': token})

    #convert json string to a python dictionary
    pack = json.loads(r.text)

    needle = pack['needle']
    haystack = pack['haystack']

    #get index of element needle, inside of list haystack
    index = haystack.index(needle)

    r = requests.post(link_validate, json = {'token': token, 'needle': index})
    print(r.text)

find_needle()
