import urllib.request
import json_stream
from customer import Customer

URL = 'https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json'


def process_item(data):
    customer = Customer(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        url=data['url'],
        type=data['type']
    )

    print(customer.__dict__)


def process_pending_notifications():
    with urllib.request.urlopen(URL) as response:
        data = json_stream.load(response, persistent=False)

        for item in data:
            process_item(item)


process_pending_notifications()