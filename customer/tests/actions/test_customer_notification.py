import pytest

from customer.actions import customer_notification
from customer.constans import NotificationType
from customer.exceptions import NotificationException


class TestCustomerNotification:

    def test_calls_send_sms_when_type_is_sms_and_has_phone(
            self, customer, mock_send_sms):
        customer.type = NotificationType.SMS
        customer.phone = '+1-089-080-9224x470'

        customer_notification.execute(customer)

        mock_send_sms.assert_called_once()

    def test_raises_exception_when_type_is_sms_and_phone_is_none(
            self, customer, mock_send_sms):
        customer.type = NotificationType.SMS
        customer.phone = None

        with pytest.raises(NotificationException):
            customer_notification.execute(customer)

        mock_send_sms.assert_not_called()

    def test_calls_send_email_when_type_is_email_and_has_email(
            self, customer, mock_send_email):
        customer.type = NotificationType.EMAIL
        customer.email = 'gabriellazamora@example.org'

        customer_notification.execute(customer)

        mock_send_email.assert_called_once()

    def test_raises_exception_when_type_is_email_and_email_is_none(
            self, customer, mock_send_email):
        customer.type = NotificationType.EMAIL
        customer.email = None

        with pytest.raises(NotificationException):
            customer_notification.execute(customer)

        mock_send_email.assert_not_called()

    def test_calls_send_post_when_type_is_post_and_has_url(
            self, customer, mock_send_post):
        customer.type = NotificationType.POST
        customer.url = 'https://esparza-alvarez.com/'

        customer_notification.execute(customer)

        mock_send_post.assert_called_once()

    def test_raises_exception_when_type_is_post_and_url_is_none(
            self, customer, mock_send_post):
        customer.type = NotificationType.POST
        customer.url = None

        with pytest.raises(NotificationException):
            customer_notification.execute(customer)

        mock_send_post.assert_not_called()

    def test_raise_exception_when_name_is_none(
           self, customer, mock_send_sms, mock_send_email, mock_send_post):
        customer.name = None

        with pytest.raises(NotificationException):
            customer_notification.execute(customer)

        mock_send_sms.assert_not_called()
        mock_send_email.assert_not_called()
        mock_send_post.assert_not_called()

    @pytest.mark.parametrize('type', [
        None,
        'postal',
    ])
    def test_raise_exception_when_type_is_not_valid(
            self, type, customer, mock_send_sms, mock_send_email,
            mock_send_post):
        customer.type = type

        with pytest.raises(NotificationException):
            customer_notification.execute(customer)

        mock_send_sms.assert_not_called()
        mock_send_email.assert_not_called()
        mock_send_post.assert_not_called()
