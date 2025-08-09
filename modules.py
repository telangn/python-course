# Core modules
import datetime
from datetime import date
import time
# Pip Module
from camelcase import CamelCase

# Custom module
import customValidatorModule
from customValidatorModule import validate_email

today = date.today()
timestamp = time.time()

c = CamelCase()

email = 'test#test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')

print(c.hump('hello there world'))
print(today, timestamp)