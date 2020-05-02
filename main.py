import script
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os
import pickle

ACCOUNT = os.getenv('ACCOUNT', None)
TOKEN = os.getenv('TOKEN', None)
TO_NUMBER = os.getenv('TO_NUMBER', None)
FROM_NUMBER = os.getenv('FROM_NUMBER', None)

if None in [ACCOUNT, TOKEN, TO_NUMBER, FROM_NUMBER]:
    raise Exception('BAD ENV CONFIG> MISSING ONE OF [ACCOUNT, TOKEN, TO_NUMBER, FROM_NUMBER]')

client = Client(ACCOUNT, TOKEN)
line = script.read()

is_complete = False
try:
    is_complete = pickle.load(open("complete.pickle", "rb"))
except (OSError, IOError) as e:
    is_complete = False
    pickle.dump(is_complete, open("complete.pickle", "wb"))

if line.strip() == 'To victory!':
    is_complete = True
    pickle.dump(is_complete, open("complete.pickle", "wb"))

if is_complete:
    print('done!')
    exit(0)
try:
    message = client.messages.create(
        to=TO_NUMBER,
        from_=FROM_NUMBER,
        body=line
    )
except TwilioRestException as e:
    print(e)
