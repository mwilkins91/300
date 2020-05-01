import script
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os

ACCOUNT = os.getenv('ACCOUNT', None)
TOKEN = os.getenv('TOKEN', None)
TO_NUMBER = os.getenv('TO_NUMBER', None)
FROM_NUMBER = os.getenv('FROM_NUMBER', None)

if None in [ACCOUNT, TOKEN, TO_NUMBER, FROM_NUMBER]:
    raise Exception('BAD ENV CONFIG> MISSING ONE OF [ACCOUNT, TOKEN, TO_NUMBER, FROM_NUMBER]')

client = Client(ACCOUNT, TOKEN)
line = script.read()

try:
    message = client.messages.create(
        to=TO_NUMBER,
        from_=FROM_NUMBER,
        body=line
    )
except TwilioRestException as e:
    print(e)
