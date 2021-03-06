import urllib.request
import json_stream

from concurrent.futures import ThreadPoolExecutor
from django.core.management import BaseCommand
from django.conf import settings
from customer.actions import customer_notification
from customer.exceptions import NotificationException
from customer.models import Customer


class Command(BaseCommand):
    help = 'Process pending notifications'

    def handle(self, *args, **options):
        with urllib.request.urlopen(settings.NOTIFICATIONS_LOG_URL) as response:
            data = json_stream.load(response, persistent=False)
            with ThreadPoolExecutor(max_workers=settings.MAX_WORKERS) as thread:
                for item in data:
                    customer = Customer(
                        name=item['name'],
                        email=item['email'],
                        phone=item['phone'],
                        url=item['url'],
                        type=item['type']
                    )
                    data_result = thread.submit(customer_notification.execute, customer)

                    try:
                        data_result.result()
                    except NotificationException:
                        print(f"We can not send notifications: {customer.to_dict()}")
