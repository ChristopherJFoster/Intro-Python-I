"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

calendar.setfirstweekday(6)
newline = '\n'

m = datetime.now().month
y = datetime.now().year

print(newline, end='')
calInput = input(
    'Please enter a numerical month and year: ').split(' ')

if calInput[0] != '':
    try:
        int(calInput[0])
    except ValueError:
        print(
            newline, f'Input should be a numerical month and year, in the form of: {m} {y}', newline)
        sys.exit()

    if int(calInput[0]) not in range(1, 13):
        print(
            newline, f'Input should be a numerical month and year, in the form of: {m} {y}', newline)
        sys.exit()
    else:
        m = int(calInput[0])

    if len(calInput) > 1:
        try:
            int(calInput[1])
        except ValueError:
            print(
                newline, f'Input should be a numerical month and year, in the form of: {m} {y}', newline)
            sys.exit()
        y = int(calInput[1])

print('\n', calendar.month(y, m))
