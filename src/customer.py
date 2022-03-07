
class Customer:
    def __init__(self, name, email, phone, url, type):
        self.name = name
        self.email = email
        self.phone = phone
        self.url = url
        self.type = type

    def has_name(self) -> bool:
        return self.name is not None

    def has_phone(self) -> bool:
        return self.phone is not None

    def has_email(self) -> bool:
        return self.email is not None

    def has_url(self) -> bool:
        return self.url is not None

    def can_send_sms(self):
        return self.has_name() and self.has_phone()

    def can_send_email(self):
        return self.has_name() and self.has_email()

    def can_send_post(self):
        return self.has_name() and self.has_url()
