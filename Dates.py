# => We often need current date and time when logging errors or saving data
# To get current date and time we use the datetime library

from datetime import datetime

current_date = datetime.now()   # now() returns a datetime object
print('Today is: ' + str(current_date))

# -------------------------------------------------------------------

# => You can use timedelta to manipulate dates
from datetime import timedelta

today = datetime.now()
print('Today is: ' + str(today))

one_day = timedelta(days=1)     # define a period of 1 day
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# -------------------------------------------------------------------

# => Access parts of a datetime object
current_date = datetime.now()

print('Day: ' + str(current_date.day))     # Day number
print('Month: ' + str(current_date.month)) # Month number
print('Year: ' + str(current_date.year))   # Year number

# -------------------------------------------------------------------

# => Sometimes you receive a date as a string and need to convert it
birthday = input('When is your birthday (dd/mm/yyyy)? : ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')  # convert string → datetime
print('Birthday: ' + str(birthday_date))