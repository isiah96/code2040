import requests
import json

'''
' Step 4
' prefix() - Retrieves a dictionary from the server containing prefix -
' a string, and array - an array of strings, creates a new array exluding
' all words that begin with prefix from the original array, then sends this
' back to the server for validation.
'''

def prefix():
    token = '5ea5ad07f90d2f12f2b36cd9e48c01ab'
    link_prefix = "http://challenge.code2040.org/api/prefix"
    link_validate = "http://challenge.code2040.org/api/prefix/validate"

    r = requests.post(link_prefix, json = {'token': token})
    pack = json.loads(r.text)

    prefix = pack['prefix']
    array = pack['array']

    #we want all words in array that don't start with prefix
    #implemented using a list comprehension
    new_array = [x for x in array if not x.startswith(prefix)]

    r = requests.post(link_validate, json = {'token': token, 'array': new_array})
    print(r.text)

prefix()
