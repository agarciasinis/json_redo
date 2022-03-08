from exercise.core import notifications
from exercise.customer.constans import NotificationType
from exercise.customer.exceptions import NotificationException
from exercise.customer.models import Customer


def execute(customer: Customer):
    if not customer.has_name():
        raise NotificationException

    if customer.type == NotificationType.SMS and customer.has_phone():
        notifications.send_sms(customer.phone, customer.to_dict())

    elif customer.type == NotificationType.EMAIL and customer.has_email():
        notifications.send_email(customer.email, customer.to_dict())

    elif customer.type == NotificationType.POST and customer.has_url():
        notifications.send_post(customer.url, customer.to_dict())

    else:
        raise NotificationException
