from constans import NotificationType
from customer import Customer


def send_notification(customer: Customer):
    if customer.type == NotificationType.SMS and customer.can_send_sms():
        send_sms(customer.phone, vars(customer))

    elif customer.type == NotificationType.EMAIL and customer.can_send_email():
        send_email(customer.email, vars(customer))

    elif customer.type == NotificationType.POST and customer.can_send_post():
        send_post(customer.url, vars(customer))


def send_sms(phone: str, data: dict) -> None:
    print(f"SMS sent to {phone}. Data: {data}")


def send_email(email: str, data: dict) -> None:
    print(f"EMAIL sent to {email}. Data: {data}")


def send_post(url: str, data: dict) -> None:
    print(f"POST sent to {url}. Data: {data}")
