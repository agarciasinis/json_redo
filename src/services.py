from constans import NotificationType
from customer import Customer


def send_notification(customer: Customer):
    if not customer.has_name():
        print('We need the name to send a notification')
        return

    if customer.type == NotificationType.SMS and customer.has_phone():
        send_sms(customer.phone, vars(customer))

    elif customer.type == NotificationType.EMAIL and customer.has_email():
        send_email(customer.email, vars(customer))

    elif customer.type == NotificationType.POST and customer.has_url():
        send_post(customer.url, vars(customer))

    else:
        send_other_type_of_notification(customer)


def send_other_type_of_notification(customer):
    if customer.has_phone():
        print(f"Type notification is {customer.type} but we send a SMS")
        send_sms(customer.phone, vars(customer))
    elif customer.has_email():
        print(f"Type notification is {customer.type} but we send an EMAIL")
        send_email(customer.email, vars(customer))
    elif customer.has_url():
        print(f"Type notification is {customer.type} but we send a POST")
        send_post(customer.url, vars(customer))
    else:
        print(f"We can not send notifications to {customer.name}: {vars(customer)}")


def send_sms(phone: str, data: dict) -> None:
    print(f"SMS sent to {phone}. Data: {data}")


def send_email(email: str, data: dict) -> None:
    print(f"EMAIL sent to {email}. Data: {data}")


def send_post(url: str, data: dict) -> None:
    print(f"POST sent to {url}. Data: {data}")
