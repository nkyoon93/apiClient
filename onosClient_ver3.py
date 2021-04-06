import requests

url = "http://192.168.0.8:8181/onos/v1/applications/org.onosproject.routescale"
body = {"": ""}
print(requests.get(url, Body=body).json())