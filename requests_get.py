import requests
import json
from pprint import pprint

router = {"ip": "172.16.69.132",
          "port": "443",
          "user": "root",
          "pass": "cisco"}

headers = {"Accept": "application/yang-data+json"}

u = "https://{}:{}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"
u = u.format(router["ip"], router["port"])

#print(u)
r = requests.get(u,
            headers = headers,
            auth=(router["user"], router["pass"]),
            verify=False)

pprint(r.text)

api_data = r.json()
pprint("/" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["ipv4"])
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["ipv4-subnet-mask"])
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
pprint("/" * 50)

if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == "if-state-up":
    pprint("interface is up")

