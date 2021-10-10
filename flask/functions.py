from datetime import datetime, date
import calendar
from functions_db import get_username_db

def birthday_msg(username, date):
    date = get_username_db(username)
    user_dob = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    today = datetime.today().strftime('%Y-%m-%d')
    today_date = datetime.strptime(today, '%Y-%m-%d')

    if today_date == user_dob:
        msg = f"Hello, {username}! Happy birthday!"
    else:
        ndays = countdiff(user_dob, today_date)
        msg = f"Hello, {username}! Your birthday is in {ndays} day(s)"

    json_msg = { "message": msg}

    return json_msg


def countdiff(user_dob, today_date):
    birthday = date(today_date.year, user_dob.month, user_dob.day)
    today = date(today_date.year, today_date.month, today_date.day)
    todaycheck = date(today_date.year, user_dob.month, user_dob.day)

    if today > todaycheck:
        monthrange = calendar.monthrange(today_date.year, today_date.month)
        toend = date(today_date.year, 12, monthrange[1])
        daystoend = abs(today - toend)
        yearolder0 = date(today_date.year + 1, 1, 1)
        yearolder1 = date(yearolder0.year, user_dob.month, user_dob.day)
        yearolderdiff = yearolder1 - yearolder0

        delta = daystoend + yearolderdiff
    else:
        delta = abs(today - birthday)
    
    return delta.days