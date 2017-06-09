import os
from flightspy import FlightsPy
from date_util import daterange  # converts start and end date into a range of dates, produces a generator
from datetime import datetime

API_KEY = os.environ.get('API_KEY')
access = FlightsPy(API_KEY)

#TODO: Get run.py to run up to 50 days beyond a date and then state the cheapest Ticket Price of the day
"""
access.grab(params={
    'origin': 'JFK',
    'destination': 'KIN',
    'date': '2017-06-03',
    'solutions': 3
    })

access.print_result()
"""

# The following is a test case for use
params = {}
params['origin'] = 'KIN'
params['destination'] = 'JFK'
params['solutions'] = 1

today = datetime.today() # If it is too late in the day QPX will return an error, can/maybe should be renamed start_date
end_date = datetime(2017, 6, 30) # some fixed date in the future TODO: have this be a set interval away from the initial start_date

for date in daterange(today, end_date):
    date = date.strftime('%Y-%m-%d') # converts date to a form that QPX can recognize
    params['date'] = date
    access.grab(params) #TODO: improve this so we won't have to call QPX API each time
    access.print_result()
