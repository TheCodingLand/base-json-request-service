import json
from project.models import Ticket
import requests

t = Ticket()
t.Title="ticket"
t.Description="ticket"

url='http://localhost' #URL ot the Server
headers = { 'Content-Type': 'text/xml', 'charset': 'utf-8' }


def createTicket(ticket):
    return requests.post(url,headers, json.dumps(t.serialize()))


print(json.dumps(t.serialize()))
  
#print(createTicket(t))
