import urllib.request
import json_stream

from django.core.management import BaseCommand

from django.conf import settings
from exercise.customer.actions import customer_notification
from exercise.customer.models import Customer


class Command(BaseCommand):
    help = 'Process pending notifications'

    def handle(self, *args, **options):
        with urllib.request.urlopen(settings.NOTIFICATIONS_LOG_URL) as response:
            data = json_stream.load(response, persistent=False)

            for item in data:
                customer = Customer(
                    name=item['name'],
                    email=item['email'],
                    phone=item['phone'],
                    url=item['url'],
                    type=item['type']
                )
                customer_notification.execute(customer)
