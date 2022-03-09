
class TestCustomer:

    def test_has_name_returns_true_when_name_has_value(self, customer):
        assert customer.has_name() is True

    def test_has_name_returns_false_when_name_is_none(self, customer):
        customer.name = None

        assert customer.has_name() is False

    def test_has_phone_returns_true_when_phone_has_value(self, customer):
        assert customer.has_name() is True

    def test_has_phone_returns_false_when_phone_is_none(self, customer):
        customer.phone = None

        assert customer.has_phone() is False

    def test_has_email_returns_true_when_email_has_value(self, customer):
        assert customer.has_email() is True

    def test_has_email_returns_false_when_email_is_none(self, customer):
        customer.email = None

        assert customer.has_email() is False

    def test_has_url_returns_true_when_url_has_value(self, customer):
        assert customer.has_url() is True

    def test_has_url_returns_false_when_url_is_none(self, customer):
        customer.url = None

        assert customer.has_url() is False

    def test_has_type_returns_true_when_type_has_value(self, customer):
        assert customer.has_url() is True

    def test_has_type_returns_false_when_type_is_none(self, customer):
        customer.url = None

        assert customer.has_url() is False

    def test_to_dict_returns_dictionary(self, customer):
        customer_dict = customer.to_dict()

        assert customer_dict == {
            'name': 'James Baker',
            'email': 'gabriellazamora@example.org',
            'phone': '+1-089-080-9224x470',
            'url': 'https://esparza-alvarez.com/',
            'type': 'post'
        }
