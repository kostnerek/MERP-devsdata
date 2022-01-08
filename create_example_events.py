import requests
import json
import db
def create_example_events():
    url = "http://127.0.0.1:5000/event"


    payload = json.dumps({
        "title": "Event1",
        "startDate": "2022-01-10T15:00:00",
        "endDate": "2022-01-10T17:00:00"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    payload = json.dumps({
        "title": "Event2",
        "startDate": "2022-01-15T15:00:00",
        "endDate": "2022-01-17T17:00:00"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    payload = json.dumps({
        "title": "Event3",
        "startDate": "2022-01-22T15:00:00",
        "endDate": "2022-01-22T15:00:00"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    url = "http://127.0.0.1:5000/event/thumbnail/Event1"

    payload={}
    files=[
        ('image',('file',open('e1.jpg','rb'),'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    url = "http://127.0.0.1:5000/event/thumbnail/Event2"

    payload={}
    files=[
        ('image',('file',open('e2.jpg','rb'),'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    url = "http://127.0.0.1:5000/event/thumbnail/Event3"

    payload={}
    files=[
        ('image',('file',open('e3.jpg','rb'),'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

if __name__ == "__main__":
    create_example_events()