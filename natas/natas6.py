#python2.7
import requests
import re
username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
url = 'http://%s.natas.labs.overthewire.org/' % username
#headers = {'Authorization': 'access_token myToken' }

#response = requests.get(url,  headers = headers,auth = (username, password))

s = requests.Session()
#s.auth = (username, password)
s.headers.update({'x-test': 'true'})

#send own cookie
cookies = {"loggedin" : "1"}

r = s.get(url, auth = (username, password), cookies = cookies)
print r.text
print 'print cookie:'
#print s.cookies['loggedin']
#content = response.text
#print content
#print re.findall('natas5 is (.*)', content)[0]