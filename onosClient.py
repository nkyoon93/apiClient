import urllib3

API_HOST = 'http://192.168.0.8:8181/onos/v1/docs/v1/devices'
API_KEY = 'karaf'

data = {}

def req(path, query, method, data={}):
    url = API_HOST + path
    print('HTTP Method: %s' %method)
    print('Request URL: %s' $url)
    print('QueryString: %s' %query)

    if 'GET' == method:
        req = urllib3.Request(API_HOST + path)

    elif 'POST' == method:
        req = urllib3.Request(API_HOST + path, data)

    req.add_header('Authorization', API_KEY)
    return  urllib3.urlopen(req)
