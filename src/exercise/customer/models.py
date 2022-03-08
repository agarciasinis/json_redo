
class Customer:
    def __init__(self, name: str, email: str, phone: str, url: str, type: str):
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

    def to_dict(self) -> dict:
        return vars(self)
