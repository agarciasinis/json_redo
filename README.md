
# Exercise
In the event of a system crash, we would like to be able to reply (resend) the notifications that have not been sent.

The program should fetch a JSON file from `https://github.com/UN-ICC/notifications-processor
/blob/master/notifications_log.json` with all the pending transactions and, based on the type of the notification, 
the code should send an email, an SMS or call a rest API (POST) with the data payload.

# Setup

Install the following dependencies:
1. pip install Django
2. pip install urllib3
3. pip install json_stream
4. pip install pytest

# Command `process_pending_notification`

To execute the command: 
1. python ./manage.py process_pending_notifications

# Test
To execute the tests:
2. python -m pytest .\customer\tests\
