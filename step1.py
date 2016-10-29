import requests

'''
' Step 1
' register_me() - Registers student for Code2040 by sending the user-specific
' token and github link in a json dictionary to the server.
'''

def register_me():
    token = '5ea5ad07f90d2f12f2b36cd9e48c01ab'
    link_register = 'http://challenge.code2040.org/api/register'
    github = 'https://github.com/isiah96/code2040'

    r = requests.post(link_register, json = {'token': token, 'github': github})
    print(r.text)

register_me()
