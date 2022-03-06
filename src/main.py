import urllib.request
import json_stream
from notification import Customer

URL = 'https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json'


def process_item(data):
    print(f"{data} - {data['name']}")


def process_pending_notifications():
    with urllib.request.urlopen(URL) as response:
        data = json_stream.load(response, persistent=False)

        for item in data:
            process_item(item)


process_pending_notifications()
