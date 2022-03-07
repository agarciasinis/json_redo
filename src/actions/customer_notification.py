from utils import notification
from constans import NotificationType
from customer import Customer


def execute(customer: Customer):
    if not customer.has_name():
        print(f"We need the name to send a notification {customer.to_dict()}")
        return

    if customer.type == NotificationType.SMS and customer.has_phone():
        notification.send_sms(customer.phone, customer.to_dict())

    elif customer.type == NotificationType.EMAIL and customer.has_email():
        notification.send_email(customer.email, customer.to_dict())

    elif customer.type == NotificationType.POST and customer.has_url():
        notification.send_post(customer.url, customer.to_dict())

    else:
        print(f"We can not send notifications to "
              f"{customer.name}: {customer.to_dict()}")
        return
