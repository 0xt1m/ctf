import requests

url = "http://valley.thm"
headers = {'Cookie':'password=secret'}
DEBUG = 0

for port in xrange(1, 65535+1):
    if DEBUG and (port%100 == 0):
        print "STATUS: Tested " + str(port) + " ports"
    r = requests.get(url + str(port), headers=headers)
    if r.status_code == requests.codes.ok :
        print "OPEN => " + str(port)