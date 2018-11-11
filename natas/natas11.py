#python2.7
import requests
import re
import urllib
import base64

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
url = 'http://%s.natas.labs.overthewire.org/' % username
#http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
#headers = {'Authorization': 'access_token myToken' }

#response = requests.get(url,  headers = headers,auth = (username, password))

s = requests.Session()
#s.auth = (username, password)
#s.headers.update({'x-test': 'true'})

#send own cookie
#cookies = {"loggedin" : "1"}

r = s.get(url, auth = (username, password))

#r = s.post(url, params = {'needle':'u /etc/natas_webpass/natas10','submit':'submit'},  auth = (username, password) )
#print r.text
#print 'print cookie:'
print s.cookies['data']
#urllib.unquote(string)
#Replace %xx escapes by their single-character equivalent.
print base64.b64decode(urllib.unquote(s.cookies['data']))

content = r.text
#print content
#print re.findall('natas8 is (.*)', content)[0]