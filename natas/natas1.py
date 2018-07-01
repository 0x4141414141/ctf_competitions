#python2.7
import requests
import re

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth = (username, password))
content = response.text

#print content
print re.findall('<!--The password for natas2 is (.*) -->', content)[0]




