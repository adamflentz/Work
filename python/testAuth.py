__author__ = 'jwpully'


import requests
import json

protocol = 'https'
host = 'eisapi.wm.edu'
port = ''

# Create session
client = requests.session()
# If retrieving key, do this, otherwise skip down
# values = dict(username='', password='')
# url = protocol + '://' + host + port + '/api-token-auth/'

# r = client.post(url, data=values, headers=dict(Referer=url, hostname='*.wm.edu'))
# print r.status_code
# json_data = json.loads(r.content)
# print json_data['token']
# json_token = json_data['token']
json_token = 'c36fc6d2780c95ed9c678ff620fd3ba49a2a3028'
# If you already have the key, just do this part, but you need to have the json_token populated with a literal
newurl = protocol + '://' + host + port + '/filedist/upload/'
headers = {'Authorization': 'Token ' + json_token, 'path':'Axiom', 'environment':'devl'}
#  headers = {'Authorization': 'Token ' + json_token}
files = dict(file=open('test.txt', 'rb'))
#  files = dict()
# values = dict(environment='devl', path='eis_it')
values = dict()
r = client.post(newurl, files=files, data=values, headers=headers)
print r.status_code

for item in r:
    print item
