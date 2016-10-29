import requests

'''
' Step 2
' reverse_string() - Retrieves a string from the server, reverses it, and sends
' it back for validation.
'''

def reverse_string():
    token = '5ea5ad07f90d2f12f2b36cd9e48c01ab'
    link_reverse = "http://challenge.code2040.org/api/reverse"
    link_validate = "http://challenge.code2040.org/api/reverse/validate"

    r = requests.post(link_reverse, json = {'token': token})
    str_norm = r.text

    #reversing string using extended slicing
    str_reverse = str_norm[::-1]

    r = requests.post(link_validate, json = {'token': token, 'string': str_reverse})
    print(r.text)

reverse_string()
